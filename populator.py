
"""
input.txt should be in format:
Page: <Page1 Title>
Subsection: <Subsection1 Title>
Resource: <Resource1 Title>
Link: <Link1 Url>
Description: <Description1 text>
Resource: <Resource2 Title>
Link: <Link2 Url>
Description: <Description2 text>
Subsection: <Subsection2 Title>
...
Page: <Page2 Title>
...

^^Empty lines in btwn don't matter
ie. this is ok

Page: <Page1 Title>

Subsection1: <Subsection1 Title>


Resource1: <Resource1 Title>
"""

def reader(fileName):

	with open(fileName) as f:
		content = f.read().splitlines()
	
	f.close()
	pageData = {}


	for line in content:
		if (line.split(" ")[0] == "Page:"):
			#title of page
			curPage = line[len("Page:") + 1:]
			#no info currently in page
			curPageInfo = {}
			#add the page to pageData
			pageData[curPage] = curPageInfo
		elif (line.split(" ")[0] == "Subsection:"):
			#title of section
			curSection = line[len("Subsection:") + 1:]
			#no info currently in section
			curSectionInfo = {}
			#add the section to the current page
			curPageInfo[curSection] = curSectionInfo
		elif (line.split(" ")[0] == "Resource:"):
			#title of resource
			curResource = line[len("Resource:") + 1:]
			#add title to curResource resource
			curResourceInfo = {}
			curResourceInfo["title"] = curResource
			#add the resource to current subsection
			curSectionInfo[curResource] = curResourceInfo
		elif (line.split(" ")[0] == "Link:"):
			#link url
			curLink = line[len("Link:") + 1:]
			#add the link to current resource
			curResourceInfo["link"] = curLink
		elif (line.split(" ")[0] == "Description:"):
			#description text
			curDesc = line[len("Description:") + 1:]
			#add the description to current resource
			curResourceInfo["description"] = curDesc
		else:
			if (len(line.split(" ")[0]) > 2):
				print("Tag: " + line.split(" ")[0] + " is not handleded.")


	return pageData


def textHelper(text):
	return text + "\n"

#configure this based on how you want page to look
def insertHTML(resource):
	test = "<a href=\"" + resource["link"] + "\" target=\"_blank\"><font color=\"red\">" + resource["title"] + "</font> </a>\n" + resource["description"] + "\n"
	return test

pageData = reader("input.txt")

f = open("output.txt", "w")

for page in pageData:
	curPage = pageData[page]
	f.write(textHelper(page))
	f.write(textHelper("======="))
	f.write("\n")
	for subsection in curPage:
		curSection = curPage[subsection]
		f.write(textHelper(subsection))
		f.write(textHelper("----------"))
		f.write("\n")
		for resource in curSection:
			curResource = curSection[resource]
			f.write(insertHTML(curResource))
			f.write("\n")

f.close()