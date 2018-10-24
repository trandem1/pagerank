
import crawler.mainCrawl as crawl
import handleGraph.createGraph as graph
import handleGraph.pageRank as pageRank
import operator

if __name__ == '__main__':
    maxNode = 10000 #max so url
    startPath = 'https://vi.wikipedia.org/wiki/Tổng_Bí_thư_Ban_Chấp_hành_Trung_ương_Đảng_Cộng_sản_Việt_Nam'
    destPaths = crawl.getAllDestLink(startPath)
    G = graph.buildDiGraph()
    graph.addEdgeToGraph(G,startPath,destPaths)
    ### add more node in the graph
    for souceUrl in destPaths :
        destUrl = crawl.getAllDestLink(souceUrl)
        if G.__len__() < maxNode:
            graph.addEdgeToGraph(G,souceUrl,destUrl)
        else:
            break
    pr = pageRank.evaluatePageRank(G,0.85)
    sortedPr = sorted(pr.items(),key=operator.itemgetter(1),reverse=True)
    # print(sortedPr)
    maxPrint = 100
    printedCheck = 0
    for k,v in sortedPr:
        printedCheck = printedCheck +1
        print(str(k) +"\t" +str(v))
        if printedCheck > maxPrint:
            break

