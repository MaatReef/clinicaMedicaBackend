from flask import Blueprint, url_for, render_template, redirect, request, session, flash


from app.controllers.index_controller import *                                  
from app.controllers.admin_controller import *
from app.models.Users import Users

def renderAdmin():
    list_adminDoctors = view_doctors()
    list_adminUsers = view_users()
    list_healthCoverage = view_healthCoverage()
    list_adminClinics = view_clinics()
    data_admin = [list_adminDoctors, list_adminUsers, list_healthCoverage, list_adminClinics]
    return data_admin