from dataclasses import dataclass
from typing import Dict, List, Union

from models.db.game_night import GameNight, Vote
from models.internal.stats import Behaviour, HostPerformance


@dataclass
class _GameNightVotes:
    game_night: GameNight
    votes: List[Vote]


class StatsCalculator:
    data: List[_GameNightVotes]

    def __init__(self, game_nights: List[GameNight], votes: List[Vote]):
        # First we cache a hierarchy of the games and votes in a fast-accessing games id dict
        data_dict: Dict[int, _GameNightVotes] = {
            gn.id: _GameNightVotes(game_night=gn, votes=[]) for gn in game_nights
        }

        # Extend data with votes
        for vote in votes:
            if vote.game_night.id() in data_dict:
                data_dict[vote.game_night.id()].votes.append(vote)

        # Convert dict to array for the client
        self.data = [gn for gn_id, gn in data_dict.items()]

    def behaviors(self) -> List[Behaviour]:
        behaviors: Dict[str, Behaviour] = {}

        for gn in self.data:
            vote_count = len(gn.votes) * 1.0
            gn_appetizer_avg = sum([vote.appetizer for vote in gn.votes]) / vote_count
            gn_main_course_avg = sum([vote.main_course for vote in gn.votes]) / vote_count
            gn_dessert_avg = sum([vote.dessert for vote in gn.votes]) / vote_count
            gn_game_avg = sum([vote.game for vote in gn.votes]) / vote_count
            gn_sum_avg = sum([vote.nonweighed_sum() for vote in gn.votes]) / vote_count
            gn_sum_weighed_avg = sum([vote.weighed_sum() for vote in gn.votes]) / vote_count

            for vote in gn.votes:
                if vote.voter not in behaviors:
                    behaviors[vote.voter] = Behaviour(user=vote.voter)

                behaviors[vote.voter].count += 1
                behaviors[vote.voter].appetizer += vote.appetizer - gn_appetizer_avg
                behaviors[vote.voter].main_course += vote.main_course - gn_main_course_avg
                behaviors[vote.voter].dessert += vote.dessert - gn_dessert_avg
                behaviors[vote.voter].game += vote.game - gn_game_avg
                behaviors[vote.voter].sum += vote.nonweighed_sum() - gn_sum_avg
                behaviors[vote.voter].sum_weighed += vote.weighed_sum() - gn_sum_weighed_avg

        # Calculate average for each user, and convert to array
        return [
            Behaviour(
                user=behavior_sum.user,
                count=behavior_sum.count,
                appetizer=behavior_sum.appetizer / behavior_sum.count,
                main_course=behavior_sum.main_course / behavior_sum.count,
                dessert=behavior_sum.dessert / behavior_sum.count,
                game=behavior_sum.game / behavior_sum.count,
                sum=behavior_sum.sum / behavior_sum.count,
                sum_weighed=behavior_sum.sum_weighed / behavior_sum.count,
            )
            for _, behavior_sum in behaviors.items()
        ]

    def host_performances(self) -> Dict[Union[str, int], Dict[str, HostPerformance]]:
        """
        Example structure: {
            "total": {
                "Ole": HostPerformance(),
                "Stian": HostPerformance(),
                ...
            },
            2022: {
                ...
            }
        }
        """
        host_performances: Dict[Union[str, int], Dict[str, HostPerformance]] = {"total": {}}

        for gn_votes in self.data:
            # Temp variables for shorter code
            gn = gn_votes.game_night
            host = gn.host
            year = gn.date.year

            # Initiate data structures if they are missing for new users and new years
            if host not in host_performances["total"]:
                host_performances["total"][host] = HostPerformance()

            if year not in host_performances:
                host_performances[year] = {}

            if host not in host_performances[year]:
                host_performances[year][host] = HostPerformance()

            # Store general stats
            host_performances["total"][host].hosted += 1
            host_performances["total"][host].total_sum += gn.sum
            host_performances[year][host].hosted += 1
            host_performances[year][host].total_sum += gn.sum

        # Calculate averages
        for _, performances in host_performances.items():
            for name, performance in performances.items():
                performance.avg = performance.total_sum / performance.hosted

        return host_performances
