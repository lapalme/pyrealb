from typing import Iterator
import datasets

dataset_name = 'GEM/sportsett_basketball'
from Game import Game


class Games:
    # save all json structures in self.games, transformation into Game instace is done lazily on indexing
    def __init__(self, split):
        self.games = {int(g["sportsett_id"]): g for g in datasets.load_dataset(dataset_name,
                                                                               split=split)}
        # uncomment the following to get idea of the data
        # print(self.games.shape)
        # print(self.games.column_names)
        # print(json.dumps(self.games[0],indent=3,ensure_ascii=False))

    def __getitem__(self, item) -> Game | None:
        if item in self.games:
            return Game(self.games[item])
        return None

    def __len__(self) -> len:
        return len(self.games)

    def __iter__(self) -> Iterator[Game]:
        return iter(self.games)
