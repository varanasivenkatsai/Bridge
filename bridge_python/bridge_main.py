#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 07:32:21 2019

@author: srivalli
"""
from bridge_features import *
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "seva_1"))


# %%
sess = driver.session()
user_features = UserFeatures(sess)
ngo_features = NgoFeatures(sess)
corp_features = CorpFeatures(sess)


# %%
# =============================================================================
# Test cases
# =============================================================================


user_1 = User(ref_id = "15020", 
                 name = "user_5020", 
                 cause_id = "12",
                 cause = "Substance Misuse",
                 city_id = "114",
                 city = "Baltimore",
                 lat = "39.29",
                 lon ="76.61",
                 state = "MD",
                 zipcode = "21201")


user_features.create_profile(user_1)
user_features.select_cause(user_1, cause_id)
user_features.vol_ngo(user_1, ngo_id)
user_features.follow_ngo(user, ngo_id)
user_features.search_ngos_by_cause(user_1, cause_id)
user_features.search_ngos_nearme(user_1)
user_features.search_events_nearme(user_1)
user_features.ngo_suggestions(user_1)
user_features.event_suggestions(user_1)



# %%
ngo_1 = Ngo(ref_id = "20250",
                 name = "ngo_250", 
                 cause_id = "12",
                 cause = "Substance Misuse",
                 city_id = "114",
                 city = "Baltimore",
                 lat = "39.29",
                 lon ="76.61",
                 state = "MD",
                 zipcode = "21201",
                 url = "www.ngo_250.com")

ngo_features.create_profile(ngo_1)

event_1 = Event( ref_id = "30150",
                 name = "event_150", 
                 cause_id = "12",
                 cause = "Substance Misuse",
                 city_id = "114",
                 city = "Baltimore",
                 lat = "39.29",
                 lon ="76.61",
                 state = "MD",
                 zipcode = "21201")

ngo_features.create_event(ngo_1, event_1)



# %%
corp_1 = Corporate(ref_id = "40200", 
                 name = "corporate_200", 
                 cause_id = "12",
                 cause = "Substance Misuse",
                 city_id = "114",
                 city = "Baltimore",
                 lat = "39.29",
                 lon ="76.61",
                 state = "MD",
                 zipcode = "21201")

corp_features.create_profile(corp_1)
corp_features.follow_ngo(corp_1, ngo_id)
corp_features.search_ngos_by_cause(corp_1, cause_id)
corp_features.search_ngos_nearme(corp_1)
