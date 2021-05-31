from list_node import ListNode
from attempt1 import Solution


class TestMerge2Lists:
    def test_0001(self):
        sol = Solution()
        list1 = ListNode.from_list([1, 13, 15, 16])
        list2 = ListNode.from_list([2, 4, 5, 7, 17])

        result = sol.merge_two_lists(list1, list2)

        assert result.to_list() == [1, 2, 4, 5, 7, 13, 15, 16, 17]

    def test_0002(self):
        sol = Solution()
        list1 = ListNode.from_list([1, 13])
        list2 = ListNode.from_list([2])

        result = sol.merge_two_lists(list1, list2)

        assert result.to_list() == [1, 2, 13]

    def test_0003(self):
        sol = Solution()
        list1 = ListNode.from_list([3, 13])
        list2 = ListNode.from_list([2])

        result = sol.merge_two_lists(list1, list2)

        assert result.to_list() == [2, 3, 13]

    def test_0004(self):
        sol = Solution()
        list1 = ListNode.from_list([3])
        list2 = ListNode.from_list([2])

        result = sol.merge_two_lists(list1, list2)

        assert result.to_list() == [2, 3]
