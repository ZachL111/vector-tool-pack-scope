import unittest

from src.vector_tool_pack_scope.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(53, 44, 22, 68)
        self.assertEqual(review_score(item), 152)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
