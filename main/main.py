
import crawler.mainCrawl as crawl
import handleGraph.createGraph as graph
import handleGraph.pageRank as pageRank
import operator

def writeToFile(fileName,startPath,numberNode,pageRanks,maxPrint = 100):
    printedCheck = 0
    f = open(fileName,"w")
    startTitle = crawl.getTitleLink(startPath)
    f.write(startTitle +"\t" + str(numberNode))
    f.write("\n")
    f.write("Pagerank"+"\t"+"Title")
    f.write("\n")
    for k,v in pageRanks:
        printedCheck = printedCheck +1
        # print(str(k) +"\t" +str(v))
        f.write(str("{:1.4f}".format(v)) +"\t" + crawl.getTitleLink(str(k)))
        f.write("\n")
        if printedCheck > maxPrint:
            break
    f.close()


if __name__ == '__main__':
    ### khoi tao tham so
    maxNode = 5000 #max so url
    startPath = 'https://vi.wikipedia.org/wiki/Tổng_Bí_thư_Ban_Chấp_hành_Trung_ương_Đảng_Cộng_sản_Việt_Nam'

    destPaths = crawl.getAllDestLink(startPath)
    G = graph.buildDiGraph()
    graph.addEdgeToGraph(G,startPath,destPaths)
    ### add more node in the graph
    for souceUrl in destPaths :
        destUrl = crawl.getAllDestLink(souceUrl)
        print("size of graph =" + str(G.__len__()))
        if G.__len__() < maxNode:
            graph.addEdgeToGraph(G,souceUrl,destUrl)
        else:
            break

    pr = pageRank.evaluatePageRank(G,0.85)

    sortedPr = sorted(pr.items(),key=operator.itemgetter(1),reverse=True)
    print("start write")
    writeToFile("20181_IT4868_Assignment01_GroupXXX_ranking.txt",startPath,G.__len__(),sortedPr,100)




