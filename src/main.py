import time
from GraphAlgo import GraphAlgo


def check1():
    print("********* G_10_80 **********")
    g = GraphAlgo()
    file = "/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_10_80_1.json"
    g.load_from_json(file)
    start = time.time()
    print(f"size of SCC of 8: {g.connected_component(8).__len__()}")
    end = time.time() - start
    print("\n SCC of 8 Run time: %.3f sec\n" % end)

    start = time.time()
    scc = g.connected_components()
    end = time.time() - start
    print(f"number of all scc: {scc.__len__()}")
    print("\n SCC Run time: %.3f sec\n" % end)

    start = time.time()
    print(g.shortest_path(1,4))
    end = time.time() - start
    print("\n Shortest path(1->4), Run time: %.3f sec" % end)
    print("*******************************")


def check2():
    print("\n********* G_100_800 **********")
    g = GraphAlgo()
    file = "/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_100_800_1.json"
    g.load_from_json(file)

    start = time.time()
    print(f"size of SCC of 66: {g.connected_component(66).__len__()}")
    end = time.time() - start
    print("\n SCC of 66 Run time: %.3f sec\n" % end)

    start = time.time()
    scc = g.connected_components()
    end = time.time() - start
    print(f"number of all scc: {scc.__len__()}")
    print("\n SCC Run time: %.3f sec" % end)

    start = time.time()
    print(g.shortest_path(5,9))
    end = time.time() - start
    print("\n Shortest path(5->9), Run time: %.3f sec" % end)

    print("*******************************")

def check3():
    print("\n********* G_1000_8000 **********")
    g = GraphAlgo()
    file = "/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_1000_8000_1.json"
    g.load_from_json(file)

    start = time.time()
    print(f"size of SCC of 44: {g.connected_component(44).__len__()}")
    end = time.time() - start
    print("\n SCC of 44 Run time: %.3f sec\n" % end)

    start = time.time()
    scc = g.connected_components()
    end = time.time() - start
    print(f"number of all scc: {scc.__len__()}")
    print("\n SCC Run time: %.3f sec\n" % end)

    start = time.time()
    print(g.shortest_path(100,500))
    end = time.time() - start
    print("\n Shortest path(100->500), Run time: %.3f sec" % end)

    print("*******************************")


def check4():
    print("\n********* G_10000_80000 **********")
    g = GraphAlgo()
    file = "/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_10000_80000_1.json"
    g.load_from_json(file)

    start = time.time()
    print(f"size of SCC of 2000: {g.connected_component(2000).__len__()}")
    end = time.time() - start
    print("\n SCC of 2000 Run time: %.3f sec\n" % end)

    start = time.time()
    scc = g.connected_components()
    end = time.time() - start
    print(f"number of all scc: {scc.__len__()}")
    print("\n SCC Run time: %.3f sec" % end)

    start = time.time()
    print(g.shortest_path(1,2000))
    end = time.time() - start
    print("\n Shortest path(1->2000), Run time: %.3f sec" % end)

    print("*******************************")


def check5():
    print("\n********* G_20000_160000 **********")
    g = GraphAlgo()
    file = "/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_20000_160000_1.json"
    g.load_from_json(file)

    start = time.time()
    print(f"size of SCC of 12000: {g.connected_component(12000).__len__()}")
    end = time.time() - start
    print("\n SCC of 12000 Run time: %.3f sec\n" % end)

    start = time.time()
    scc = g.connected_components()
    end = time.time() - start
    print(f"number of all scc: {scc.__len__()}")
    print("\n SCC Run time: %.3f sec" % end)

    start = time.time()
    print(g.shortest_path(1000,6500))
    end = time.time() - start
    print("\n Shortest path(1000->6500), Run time: %.3f sec" % end)

    print("*******************************")


def check6():
    print("\n********* G_30000_240000 **********")
    g = GraphAlgo()
    file = "/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_30000_240000_1.json"
    g.load_from_json(file)

    start = time.time()
    print(f"size of SCC of 28000{g.connected_component(28000).__len__()}")
    end = time.time() - start
    print("\n SCC of 28000 Run time: %.3f sec\n" % end)

    start = time.time()
    scc = g.connected_components()
    end = time.time() - start
    print(f"number of all scc: {scc.__len__()}")
    print("\n SCC Run time: %.3f sec" % end)

    start = time.time()
    print(g.shortest_path(12345,24678))
    end = time.time() - start
    print("\n Shortest path(12345->24678), Run time: %.3f sec" % end)

    print("*******************************")

def plot():
    g = GraphAlgo()
    file = "/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_10_80_1.json"
    g.load_from_json(file)
    g.plot_graph()


if __name__ == '__main__':
    # plot()
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()
