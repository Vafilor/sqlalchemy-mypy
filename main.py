from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    Session,
    declarative_mixin,
    declared_attr,
    mapped_column,
    relationship,
)


class Base(MappedAsDataclass, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]


@declarative_mixin
class UserMixin:
    user_id = mapped_column(ForeignKey("users.id"))

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship("User", kw_only=True)


class Task(UserMixin, Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]


# None is added as the return value to make sure mypy checks this
# From mypy: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
def main() -> None:
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        user = User(name="user")

        # error: Unexpected keyword argument "user" for "Task"  [call-arg]
        task = Task(name="Submit issue", user=user)

        session.add_all([user, task])
        session.commit()


if __name__ == "__main__":
    main()
