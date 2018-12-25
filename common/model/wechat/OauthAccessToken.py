from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class OauthAccessToken(db.Model):
    __tablename__ = 'oauth_access_token'

    id = db.Column(Integer, primary_key=True)
    access_token = db.Column(String(600), nullable=False, server_default=FetchedValue())
    expired_time = db.Column(DateTime, nullable=False, index=True, server_default=FetchedValue())
    created_time = db.Column(DateTime, nullable=False, server_default=FetchedValue())
