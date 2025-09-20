from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False)
    authentication_string = Column(String(255), nullable=False)

    tokens = relationship("AuthToken", back_populates="user")


class AuthToken(Base):
    __tablename__ = 'auth_tokens'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service = Column(String(255), nullable=False)
    scope = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False)

    user = relationship("User", back_populates="tokens")


class Workflow(Base):
    __tablename__ = 'workflows'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(512), nullable=True)

    nodes = relationship("WorkflowNode", back_populates="workflow")


class WorkflowNode(Base):
    __tablename__ = 'workflow_nodes'

    id = Column(Integer, primary_key=True)
    workflow_id = Column(Integer, ForeignKey('workflows.id'), nullable=False)
    node_type = Column(String(16), nullable=False)
    content = Column(String(16), nullable=False)
    parent_id = Column(Integer, ForeignKey('workflow_nodes.id'), nullable=True)

    workflow = relationship("Workflow", back_populates="nodes")
    parent = relationship("WorkflowNode", remote_side=[id], backref="children")
