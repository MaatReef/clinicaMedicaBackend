from flask import Blueprint, url_for, render_template, redirect, request, session, flash
from flask_login import login_user, login_required, logout_user, current_user
# from flask_session import Session
from app import login_manager

@login_manager.user_loader
def load_user(userSession):
    print("loading user")
    for user in userSession:
        session['user_dni'] = user['dni']
        session['user_name'] = user['name']