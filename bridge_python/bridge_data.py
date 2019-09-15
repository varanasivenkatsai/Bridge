# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 07:09:07 2019

@author: keert
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import random


#Creating city and cause lists to link them to other entities

city = pd.read_csv('csv_files/cities.csv')
city = city[['city_id','city', 'latitude', 'longitude', 'state', 'zip']].values
cities_meet = [list(x) for x in city]

causes = pd.read_csv('csv_files/causes.csv')
causes = causes[['category_id','category_name']].values
cause_meet = [list(x) for x in causes]

# %% 

# Global variables

number_of_users = 5000
user_starting_id = 10000

number_of_ngos = 100
ngo_starting_id = 20000

number_of_events = 100
event_starting_id = 30000

number_of_corporates = 50
corporate_starting_id = 40000


number_of_issues = 200
issues_starting_id = 50000

# %% 
    
# Creating USER entities


def user_data(number_of_users = 5000, user_starting_id = 10000):
    
    
    user_id = np.arange(user_starting_id, user_starting_id + number_of_users)
    
    user_name = []
    
    for i in range(len(user_id)):
        user_name.append("user_" + str(i))
        
    user_location = []
    
    for i in range(len(user_id)):
        user_location.append(random.choice(cities_meet))
        
    user_category = []
    
    for i in range(len(user_id)):
        user_category.append(random.choice(cause_meet))
        
    
    user_name = np.array(user_name).reshape(len(user_id),1)
    user_id = np.array(user_id).reshape(len(user_id),1)
    user_location = np.array(user_location).reshape(len(user_id),6)
    user_category = np.array(user_category).reshape(len(user_id),2)
    
    users = np.concatenate((user_id, user_name, user_category, user_location), axis = 1)
    
    users_pd = {'user_id': users[:,0],
                'user_name': users[:,1],
                'user_cause_id': users[:,2],
                'user_cause': users[:,3],
                'user_city_id': users[:,4],
                'user_city': users[:,5],
                'user_lat': users[:,6],
                'user_lon':users[:,7],
                'user_state': users[:,8],
                'user_zip': users[:,9]}
    
    users_pd = pd.DataFrame(data=users_pd)
    
    users_pd.to_csv('csv_files/users.csv')

# %% 
    
# Creating NGO entities

def ngo_data(number_of_ngos = 100, ngo_starting_id = 20000):
    
    
    ngo_id = np.arange(ngo_starting_id, ngo_starting_id + number_of_ngos)
    
    ngo_name = []
    
    for i in range(len(ngo_id)):
        ngo_name.append("ngo_" + str(i))
        
    ngo_link = []
    
    for i in range(len(ngo_id)):
        ngo_link.append("www.ngo_" + str(i) + ".com")
        
    ngo_location = []
    
    for i in range(len(ngo_id)):
        ngo_location.append(random.choice(cities_meet))
        
    ngo_category = []
    
    for i in range(len(ngo_id)):
        ngo_category.append(random.choice(cause_meet))
        
    
    ngo_name = np.array(ngo_name).reshape(len(ngo_id),1)
    ngo_id = np.array(ngo_id).reshape(len(ngo_id),1)
    ngo_location = np.array(ngo_location).reshape(len(ngo_id),6)
    ngo_category = np.array(ngo_category).reshape(len(ngo_id),2)
    
    ngo_link = np.array(ngo_link).reshape(len(ngo_id),1)
    
    ngo = np.concatenate((ngo_id, ngo_name, ngo_category, ngo_link, ngo_location), axis = 1)
    
    ngo_pd = {'ngo_id': ngo[:,0],
                'ngo_name': ngo[:,1],
                'ngo_cause_id': ngo[:,2],
                'ngo_cause':ngo[:,3],
                'ngo_link': ngo[:,4],
                'ngo_city_id': ngo[:,5],
                'ngo_city': ngo[:,6],
                'ngo_lat': ngo[:,7],
                'ngo_lon':ngo[:,8],
                'ngo_state': ngo[:,9],
                'ngo_zip': ngo[:,10]}
    
    ngo_pd = pd.DataFrame(data=ngo_pd)
    
    ngo_pd.to_csv('csv_files/ngo.csv')
    
    
# %% 
    
# Creating USERS-NGO relationships

user_id = np.arange(user_starting_id, user_starting_id + number_of_users)
    
ngo_id = np.arange(ngo_starting_id, ngo_starting_id + number_of_ngos)


user_ngo_roles = ['follows', 'follows','follows','follows','follows','follows','follows','follows','follows','volunteers']

user_ngo = []

for i in range(len(user_id)):
    for j in range(np.random.randint(1,5)):
        user_ngo.append([user_id[i],random.choice(ngo_id), random.choice(user_ngo_roles)])

user_ngo = np.array(user_ngo)

user_ngo_pd = {'user_id': user_ngo[:,0],
                'ngo_id': user_ngo[:,1],
                'role': user_ngo[:,2]}

user_ngo_pd = pd.DataFrame(user_ngo_pd)
user_ngo_pd.to_csv('csv_files/user_ngo.csv')

# %% 
    
# Creating EVENTS entities
        

def event_data(number_of_events = 100, event_starting_id = 30000):
    
    
    event_id = np.arange(event_starting_id, event_starting_id + number_of_events)
    
    event_name = []
    
    for i in range(len(event_id)):
        event_name.append("event_" + str(i))
        
    event_location = []
    
    for i in range(len(event_id)):
        event_location.append(random.choice(cities_meet))
        
    event_category = []
    
    for i in range(len(event_id)):
        event_category.append(random.choice(cause_meet))
        
    
    event_name = np.array(event_name).reshape(len(event_id),1)
    event_id = np.array(event_id).reshape(len(event_id),1)
    event_location = np.array(event_location).reshape(len(event_id),6)
    event_category = np.array(event_category).reshape(len(event_id),2)
    
    events = np.concatenate((event_id, event_name, event_category, event_location), axis = 1)
    
    events_pd = {'event_id': events[:,0],
                'event_name': events[:,1],
                'event_cause_id': events[:,2],
                'event_cause': events[:,3],
                'event_city_id': events[:,4],
                'event_city': events[:,5],
                'event_lat': events[:,6],
                'event_lon':events[:,7],
                'event_state': events[:,8],
                'event_zip': events[:,9]}
    
    events_pd = pd.DataFrame(data=events_pd)
    
    events_pd.to_csv('csv_files/events.csv')


# %%
    
# NGO-EVENT relation


ngo_id = list(np.arange(ngo_starting_id, ngo_starting_id + number_of_ngos))

event_id = list(np.arange(event_starting_id, event_starting_id + number_of_events))

event_id_shuffled = list(random.sample(event_id, k=len(event_id)))

event_type = ["virtual", "physical", "physical", "physical"]

ngo_event = []


for i in range(len(event_id_shuffled)):
    ngo_event.append([ngo_id[i], event_id_shuffled[i], random.choice(event_type)])


ngo_event = np.array(ngo_event)

ngo_event_pd = {'ngo_id': ngo_event[:,0],
                'event_id': ngo_event[:,1],
                'type': ngo_event[:,2]}

ngo_event_pd = pd.DataFrame(ngo_event_pd)
ngo_event_pd.to_csv('csv_files/ngo_event.csv')

# %%


# Creating USERS-EVENT relationships

user_id = list(np.arange(user_starting_id, user_starting_id + number_of_users))
    
event_id = list(np.arange(event_starting_id, event_starting_id + number_of_events))


user_event_roles = ['interested_in', 'interested_in','interested_in','interested_in','interested_in','interested_in','interested_in','interested_in','interested_in','going']

user_event = []

for i in range(len(user_id)):
    for j in range(np.random.randint(1,5)):
        user_event.append([user_id[i],random.choice(event_id), random.choice(user_event_roles)])

user_event = np.array(user_event)

user_event_pd = {'user_id': user_event[:,0],
                'event_id': user_event[:,1],
                'decision': user_event[:,2]}

user_event_pd = pd.DataFrame(user_event_pd)
user_event_pd.to_csv('csv_files/user_events.csv')

# %% 
    
# Creating CORPORATE entities
        

def corporate_data(number_of_corporates = 50, corporate_starting_id = 40000):
    
    
    corporate_id = np.arange(corporate_starting_id, corporate_starting_id + number_of_corporates)
    
    corporate_name = []
    
    for i in range(len(corporate_id)):
        corporate_name.append("corporate_" + str(i))
        
    corporate_location = []
    
    for i in range(len(corporate_id)):
        corporate_location.append(random.choice(cities_meet))
        
    corporate_category = []
    
    for i in range(len(corporate_id)):
        corporate_category.append(random.choice(cause_meet))
        
    
    corporate_name = np.array(corporate_name).reshape(len(corporate_id),1)
    corporate_id = np.array(corporate_id).reshape(len(corporate_id),1)
    corporate_location = np.array(corporate_location).reshape(len(corporate_id),6)
    corporate_category = np.array(corporate_category).reshape(len(corporate_id),2)
    
    corporates = np.concatenate((corporate_id, corporate_name, corporate_category, corporate_location), axis = 1)
    
    corporates_pd = {'corporate_id': corporates[:,0],
                'corporate_name': corporates[:,1],
                'corporate_cause_id': corporates[:,2],
                'corporate_cause': corporates[:,3],
                'corporate_city_id': corporates[:,4],
                'corporate_city': corporates[:,5],
                'corporate_lat': corporates[:,6],
                'corporate_lon':corporates[:,7],
                'corporate_state': corporates[:,8],
                'corporate_zip': corporates[:,9]}
    
    corporates_pd = pd.DataFrame(data=corporates_pd)
    
    corporates_pd.to_csv('csv_files/corporates.csv')
    
    
# %%


# Creating USERS-CORPORATE relationships

user_id = np.arange(user_starting_id, user_starting_id + number_of_users)
    
corporate_id = np.arange(corporate_starting_id, corporate_starting_id + number_of_corporates)


user_corporate_roles = ['employee', 'employee', 'follows']

user_corporate = []

for i in range(len(user_id)):
    for j in range(np.random.randint(0,2)):
        user_corporate.append([user_id[i],random.choice(corporate_id), random.choice(user_corporate_roles)])

user_corporate = np.array(user_corporate)

user_corporate_pd = {'user_id': user_corporate[:,0],
                'corporate_id': user_corporate[:,1],
                'role': user_corporate[:,2]}

user_corporate_pd = pd.DataFrame(user_corporate_pd)
user_corporate_pd.to_csv('csv_files/user_corporate.csv')

# %%


# Creating NGO-CORPORATE relationships

ngo_id = np.arange(ngo_starting_id, ngo_starting_id + number_of_ngos)
    
corporate_id = np.arange(corporate_starting_id, corporate_starting_id + number_of_corporates)


ngo_corporate_types = ['follows', 'follows', 'funds', 'follows']

ngo_corporate = []

for i in range(len(corporate_id)):
    for j in range(np.random.randint(1,10)):
        ngo_corporate.append([corporate_id[i],random.choice(ngo_id), 
                              random.choice(ngo_corporate_types)])

ngo_corporate = np.array(ngo_corporate)

ngo_corporate_pd = {'corporate_id': ngo_corporate[:,0],
                'ngo_id': ngo_corporate[:,1],
                'type': ngo_corporate[:,2]}

ngo_corporate_pd = pd.DataFrame(ngo_corporate_pd)
ngo_corporate_pd.to_csv('csv_files/ngo_corporate.csv')

# %%


# Creating ISSUE entities
        

def issue_data(number_of_issues = 200, issue_starting_id = 50000):
    
    
    issue_id = np.arange(issue_starting_id, issue_starting_id + number_of_issues)
    
    issue_name = []
    
    for i in range(len(issue_id)):
        issue_name.append("issue_" + str(i))
        
    issue_desc = []
    
    for i in range(len(issue_id)):
        issue_desc.append("issue_description" + str(i))
        
    issue_location = []
    
    for i in range(len(issue_id)):
        issue_location.append(random.choice(cities_meet))
        
    issue_category = []
    
    for i in range(len(issue_id)):
        issue_category.append(random.choice(cause_meet))
        
    
    issue_name = np.array(issue_name).reshape(len(issue_id),1)
    issue_id = np.array(issue_id).reshape(len(issue_id),1)
    issue_desc = np.array(issue_desc).reshape(len(issue_id),1)
    issue_location = np.array(issue_location).reshape(len(issue_id),6)
    issue_category = np.array(issue_category).reshape(len(issue_id),2)
    
    issues = np.concatenate((issue_id, issue_name, issue_category, issue_location, issue_desc), axis = 1)
    
    issues_pd = {'issue_id': issues[:,0],
                'issue_name': issues[:,1],
                'issue_cause_id': issues[:,2],
                'issue_cause': issues[:,3],
                'issue_city_id': issues[:,4],
                'issue_city': issues[:,5],
                'issue_lat': issues[:,6],
                'issue_lon':issues[:,7],
                'issue_state': issues[:,8],
                'issue_zip': issues[:,9],
                'issue_description': issues[:,10]}
    
    issues_pd = pd.DataFrame(data=issues_pd)
    
    issues_pd.to_csv('csv_files/issues.csv')
    
    
# %%
    

# Creating USERS-ISSUE_creator relationships

user_id = np.arange(user_starting_id, user_starting_id + number_of_users)
    
issue_id = np.arange(issues_starting_id, issues_starting_id + number_of_issues)


user_issue_create = []

for i in range(len(issue_id)):
    for j in range(1):
        user_issue_create.append([issue_id[i], random.choice(user_id)])

user_issue_create = np.array(user_issue_create)

user_issue_create_pd = {'issue_id': user_issue_create[:,0],
                'user_id': user_issue_create[:,1]}

user_issue_create_pd = pd.DataFrame(user_issue_create_pd)
user_issue_create_pd.to_csv('csv_files/user_issue_creator.csv')
 


# Creating USERS-ISSUE_creator relationships

user_issue_roles = ['supports']

user_issue = []

for i in range(len(user_id)):
    for j in range(np.random.randint(0,5)):
        user_issue.append([user_id[i], random.choice(issue_id), user_issue_roles[0]])

user_issue = np.array(user_issue)

user_issue_pd = {'user_id': user_issue[:,0],
                'issue_id': user_issue[:,1],
                'role': user_issue[:,2]}

user_issue_pd = pd.DataFrame(user_issue_pd)
user_issue_pd.to_csv('csv_files/user_issue_support.csv')

# %%
