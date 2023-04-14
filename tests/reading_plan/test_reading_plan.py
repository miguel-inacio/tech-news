from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501

from tests.reading_plan.mocked_news import mocked_news
import pytest
from unittest.mock import patch

# Fontes:
# https://towardsdatascience.com/python-exception-test-290366618e7d
# https://www.freblogg.com/pytest-functions-mocking-1


def test_reading_plan_group_news():

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    with patch.object(
        ReadingPlanService, "_db_news_proxy", return_value=mocked_news
    ):
        result = ReadingPlanService.group_news_for_available_time(4)
        expected = {
            "readable": [
                {
                    "unfilled_time": 1,
                    "chosen_news": [
                        (
                            mocked_news[1]["title"],
                            mocked_news[1]["reading_time"],
                        ),
                        (
                            mocked_news[2]["title"],
                            mocked_news[2]["reading_time"],
                        ),
                    ],
                }
            ],
            "unreadable": [
                (mocked_news[0]["title"], mocked_news[0]["reading_time"]),
                (mocked_news[3]["title"], mocked_news[3]["reading_time"]),
                (mocked_news[4]["title"], mocked_news[4]["reading_time"]),
            ],
        }
        assert expected == result
