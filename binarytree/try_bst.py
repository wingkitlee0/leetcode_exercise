import logging

from binarytree.bst import BSTNode

logger = logging.getLogger(__name__)


def setup_logging(level: str = "DEBUG"):

    root_logger = logging.getLogger("")
    root_logger.setLevel(level=level)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(getattr(logging, level.upper()))

    root_logger.addHandler(stream_handler)


if __name__ == "__main__":
    setup_logging()

    for i, x in enumerate([5, 3, 2, 4, 7, 6]):
        if i == 0:
            logger.info("Creating root BSTNode")
            root = BSTNode(x)
        else:
            logger.info("Adding node %s", x)
            root.addNode(x)

    root.print()
    root.print_tree_by_level()
    root.printTree_bfs2()

    print("DFS:")
    root.print_tree_by_dfs()
