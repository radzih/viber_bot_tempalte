from dataclasses import dataclass
from pathlib import Path

from environs import Env


@dataclass
class ViberBot:
    token: str
    admin_ids: list[int]
    webhook_url: str


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    bot: ViberBot
    misc: Miscellaneous



def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    
    return Config(
        bot=ViberBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            webhook_url=env.str("WEBHOOK_URL"),
        ),
        misc=Miscellaneous(
        )
    )
