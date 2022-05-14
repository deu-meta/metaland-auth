from mtl_accounts.database.schema import Minecraft_Account, Users
from mtl_accounts.models import MinecraftToken, UserToken
from sqlalchemy.orm import Session


def create_users(session: Session, user: UserToken) -> Users:
    users = Users(mail=user.email, displayName=user.display_name, givenName=user.given_name, jobTitle=user.job_title, provider=user.provider)
    session.add(users)
    session.commit()
    session.refresh(users)

    return users


def create_mincraft(session: Session, minecraft: MinecraftToken, mail: str) -> Minecraft_Account:
    users = Minecraft_Account(id=minecraft.id, user_mail=mail, provider=minecraft.provider, displayName=minecraft.displayName)
    session.add(users)
    session.commit()
    session.refresh(users)

    return users
