from typing import Iterator
import datasets

dataset_name = 'GEM/sportsett_basketball'
from Game import Game


class Games:
    # save all json structures in self.games
    def __init__(self, split):
        self.games = {g["sportsett_id"]: Game(g) for g in datasets.load_dataset(dataset_name,split=split)}

    def __getitem__(self, key:str) -> Game | None:
        if key in self.games:
            return self.games[key]
        return None

    def __len__(self) -> int:
        return len(self.games)

    def __iter__(self) -> Iterator[Game]:
        return iter(self.games)

    def keys(self) -> [str]:
        return list(self.games.keys())


if __name__ == "__main__":
    games = Games("train")
    print(games["1"].show())