#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 04:30:15 2019

@author: srivalli
"""

# %%
# [START custom_class_def]
class User(object):
    def __init__(self, ref_id, 
                 name, 
                 cause_id = 0,
                 cause,
                 city_id,
                 city,
                 lat,
                 lon,
                 state,
                 zipcode,
                 list_vol_ngo_ids = [],
                 list_follow_ngo_ids = [], 
                 list_event_ids = [],
                 list_event_maybe_ids = [],
                 list_person_ids = [],
                 list_follow_corp_ids = []):
        
        self.ref_id = ref_id
        self.name = name
        self.cause_id = cause_id
        self.cause = cause
        self.city_id = city_id
        self.city = city
        self.lat = lat
        self.lon = lon
        self.state = state
        self.zipcode = zipcode
        self.list_vol_ngo_ids= list_vol_ngo_ids
        self.list_follow_ngo_ids= list_follow_ngo_ids
        self.cause_id = cause_id
        self.list_event_ids = list_event_ids 
        self.list_event_maybe_ids = list_event_maybe_ids
        self.list_person_ids = list_person_ids
        self.list_follow_corps_ids = list_follow_corp_ids
        


    def to_dict(self):
        # [START_EXCLUDE]
        dest = {u'user_id' : self.ref_id,
                u'user_name': self.name,
                u'user_cause_id' : self.cause_id,
                u'user_cause': self.cause,
                u'user_city_id' :self.city_id,
                u'user_city' : self.city,
            u'user_lat': self.location['latitude'],
            u'user_lon': self.location['longitude'],
            u'user_state' : self.state,
            u'user_zip' : self.zipcode            
        }
        return dest
        # [END_EXCLUDE]

# [START custom_class_def]
class Ngo(object):
    def __init__(self, ref_id, 
                 name, 
                 cause_id,
                 url, 
                 city_id,
                 city,
                 lat,
                 lon,
                 state,
                 zipcode,
                 list_event_ids = []):
        
        
        self.ref_id = ref_id
        self.name = name
        self.cause_id = cause_id
        self.cause = cause
        self.url = url
        self.city_id = city_id
        self.city = city
        self.lat = lat
        self.lon = lon
        self.state = state,
        self.zipcode = zipcode
        self.list_event_ids = list_event_ids        


    def to_dict(self):
        # [START_EXCLUDE]
        dest = {u'ngo_id' : self.ref_id,
                u'ngo_name': self.name,
                u'ngo_cause_id': self.cause_id,
                u'ngo_cause' : self.cause,
                u'ngo_link' : self.url,
                u'ngo_city_id' :self.city_id,
                u'ngo_city': self.city,
                u'lat': self.lat,
                u'lon': self.lon,
                u'state' : self.state,
                u'zipcode' : self.zipcode 
        }
        return dest
        # [END_EXCLUDE]


# [END custom_class_def]
# %%
class Corporate(object):
    def __init__(self, ref_id, 
                 name, 
                 cause_id = 0,
                 cause,
                 city_id,
                 city,
                 lat,
                 lon,
                 state,
                 zipcode,
                 list_sponsor_ngo_ids = [],
                 list_follow_ngo_ids = [], 
                 list_cause_ids = []):
        
        
        self.ref_id = ref_id
        self.name = name
        self.cause_id = cause_id
        self.cause = cause
        self.city_id = city_id
        self.city = city
        self.lat = lat
        self.lon = lon
        self.state = state
        self.zipcode = zipcode
        self.list_sponsor_ngo_ids= list_sponsor_ngo_ids
        self.list_follow_ngo_ids= list_follow_ngo_ids
        self.list_cause_ids = list_cause_ids      


    def to_dict(self):
        # [START_EXCLUDE]
        dest = {u'corporate_id' : self.ref_id,
                u'corporate_name': self.name,
                u'corporate_cause_id' : self.cause_id,
                u'corporate_cause': self.cause,
                u'corporate_city_id' :self.city_id,
                u'corporater_city' : self.city,
            u'corporate_lat': self.lat,
            u'corporate_lon': self.lon,
            u'corporate_state' : self.state,
            u'corporate_zip' : self.zipcode            
        }
        return dest
        # [END_EXCLUDE]

        
# %%
class Event(object):
    def __init__(self, ref_id, 
                 name, 
                 cause_id = 0,
                 cause,
                 city_id,
                 city,
                 lat,
                 lon,
                 state,
                 zipcode):
        
        self.ref_id = ref_id
        self.name = name
        self.cause_id = cause_id
        self.cause = cause
        self.city_id = city_id
        self.city = city
        self.lat = lat
        self.lon = lon
        self.state = state
        self.zipcode = zipcode
    


    def to_dict(self):
        # [START_EXCLUDE]
        dest = {u'event_id' : self.ref_id,
                u'event_name': self.name,
                u'event_cause_id' : self.cause_id,
                u'event_cause': self.cause,
                u'event_city_id' :self.city_id,
                u'event_city' : self.city,
            u'event_lat': self.lat,
            u'event_lon': self.lon,
            u'event_state' : self.state,
            u'event_zip' : self.zipcode            
        }
        return dest
        # [END_EXCLUDE]



# %%
class Issue(object):
    def __init__(self, ref_id, 
                 name, 
                 cause_id = 0,
                 cause,
                 city_id,
                 city,
                 lat,
                 lon,
                 state,
                 zipcode,
                 description):
        
        self.ref_id = ref_id
        self.name = name
        self.cause_id = cause_id
        self.cause = cause
        self.city_id = city_id
        self.city = city
        self.lat = lat
        self.lon = lon
        self.state = state
        self.zipcode = zipcode
    


    def to_dict(self):
        # [START_EXCLUDE]
        dest = {u'issue_id' : self.ref_id,
                u'issue_name': self.name,
                u'issue_cause_id' : self.cause_id,
                u'issue_cause': self.cause,
                u'issue_city_id' :self.city_id,
                u'issue_city' : self.city,
            u'issue_lat': self.lat,
            u'issue_lon': self.lon,
            u'issue_state' : self.state,
            u'issue_zip' : self.zipcode            
        }
        return dest
        # [END_EXCLUDE]

# %%


class UserFeatures(object):
    
    def create_profile(self, user):
        self.show_node(user.to_dict())
        self.show_cred_lnks(user.ref_id, user.city_id, user.cause_id)
        return 
    
    def sign_in(self):
        return    
    
    def update_profile(self, user, name = None, lat = None, lon = None, city_id = None, corp_id= None):
        
        if name:
            user.name = name        
        if lat:
            user.lot = lat 
        if lon:
            user.location = lon
        if city_id:
            user.city_id = city_id            
            
        self.show_updated_node(user.to_dict())
        
        return    
    
    def vol_ngo(self , user, ngo_id):       
        user.list_vol_ngo_ids.append(ngo_id)
        self.show_vol_ngo_lnk(user.ref_id , ngo_id)
        return

    
    def follow_ngo(self , user, ngo_id):       
        user.list_follow_ngo_ids.append(ngo_id)
        self.show_follow_ngo_lnk(user.ref_id , ngo_id)
        return  
    
    def follow_corp(self , user, corp_id):       
        user.list_follow_corp_ids.append(corp_id)
        self.show_follow_corp_lnk(user.ref_id , corp_id)
        return  
    
    def follow_person(self, user, other_user_id):
        user.list_person_ids.append(other_user_id)
        self.show_follow_person_lnk(user.ref_id, other_user_id)
        return  
    
    def attend_event(self, user, event_id):
        user.list_event_ids.append(event_id)
        self.show_attend_event_lnk(user.ref_id, event_id)
        return          
    
    def maybe_event(self, user, event_id):
        user.list_event_maybe_ids.append(event_id)
        self.show_maybe_event_lnk(user.ref_id, event_id)
        return
    
    
    def select_cause(self, user, cause_id):
        user.list_cause_ids.append(cause_id)
        self.show_liked_cause(user.ref_id, cause_id)
        return
    
    def search_by_id(self, user, search_id):
        self.show_search_results(search_id)
        return  
    
    def search_ngos_by_cause(self, user, cause_id):
        self.show_ngos_by_cause(cause_id)
        return 
    
    def search_ngos_nearme(self, user):
        self.show_ngos_nearme(user.city_id)
        return 
    
    def search_events_nearme(self, user):
        self.show_events_nearme(user.city_id)
        return   
    
    def ngo_suggestions(self, user):
        self.show_ngos_recommended(user.ref_id)
        return user.to_dict() 
    
    def people_suggestions(self, user):
        self.show_people_recommended(user.ref_id)
        return user.to_dict() 
    
    def issue_suggestions(self, user):
        self.show_issues_recommended(user.ref_id)  
        return
        
    def support_issue(self, user, issue_id):
        user.list_support_issue_ids.append(issue_id)
        self.show_support_issue_lnk(user.ref_id , issue_id)
        return
    
    def event_suggestions(self, user):
        self.show_events_recommended(user.ref_id)
        return        
        
    def raise_issue(self, issue):        
        self.show_issue_node(issue.to_dict())
        self.show_create_issue_lnk(issue.user_id, issue.ref_id)
        self.show_issue_notif(issue.ref_id, issue.cause_id)
        return
    
# =============================================================================
#     visualization functions : Graph database
# =============================================================================
    def show_node(self, user_dict): 
        

        query = "CREATE (a:users {user_name:{u_name}, user_id:{u_id}, user_lat:{u_lat}, user_lon:{u_lon}, user_city_id: {u_city_id}, user_cause_id: {u_cause_id}, user_city_name: {u_city_name}, user_cause_name: {u_cause_name}, user_state :{u_state}, user_zip: {u_zip}})"
        self.sess.run(query, u_name= user_dict['user_name'] , u_id = user_dict['user_id'], 
                      u_lat = user_dict['user_lat'], u_lon = user_dict['user_lon'],
                      u_city_id = user_dict['user_city_id'], 
                      u_cause_id = user_dict['user_cause_id'],
                      u_city_name = user_dict['user_city_name'], 
                      u_cause_name = user_dict['user_cause_name'],
                      u_state = user_dict['user_state'],
                      u_zip = user_dict['user_zip'])
        
        print("User node created with attributes in the graph database")
        
        return
    
    def show_cred_lnks(self, user_id, city_id, cause_id):
        
        
        #user-city
        query = '''OPTIONAL MATCH (n:users {user_id: {u_id}}), (ic:cities {city_id: {ci_id}) 
        CREATE (n)-[:LOCATED_IN]->(ic)'''
        self.sess.run(query, u_id = user_id, ci_id = city_id)

        #user-cause
        query = '''OPTIONAL MATCH (n:users {user_id: {u_id}}), (ic:causes {cause_id: {co_id}) 
        CREATE (n)-[:SUPPORTS_CAUSE]->(ic)'''
        self.sess.run(query, u_id = user_id, co_id = cause_id)
        
        
        return
    
    def show_issue_node(self, issue_dict):
        
        query = "CREATE (a:issues {issue_name:{u_name}, issue_id:{u_id}, issue_lat:{u_lat}, issue_lon:{u_lon}, issue_city_id: {u_city_id}, issue_cause_id: {u_cause_id}, issue_city_name: {u_city_name}, issue_cause_name: {u_cause_name}, issue_state :{u_state}, issue_zip: {u_zip}, issue_description: {u_desc}})"
        self.sess.run(query, u_name= issue_dict['issue_name'] , u_id = issue_dict['issue_id'], 
                      u_lat = issue_dict['issue_lat'], u_lon = issue_dict['issue_lon'],
                      u_city_id = issue_dict['issue_city_id'], 
                      u_cause_id = issue_dict['issue_cause_id'],
                      u_city_name = issue_dict['issue_city_name'], 
                      u_cause_name = issue_dict['issue_cause_name'],
                      u_state = issue_dict['issue_state'],
                      u_zip = issue_dict['issue_zip'],
                      u_desc = issue_dict['issue_description'])
        
        print("issue node created with attributes in the graph database")
        return
    

    def show_follow_ngo_lnk(self,user_id, ngo_id):
        
        #user-ngo
        query = '''OPTIONAL MATCH (n:users {user_id: {u_id}}), (ic:npo {ngo_id: {n_id}) 
        CREATE (n)-[:FOLLOWS]->(ic)'''
        self.sess.run(query, u_id = user_id, n_id = ngo_id)
        
        return

    def show_liked_cause(self, user_id, cause_id):
        
        #user-cause
        query = '''OPTIONAL MATCH (n:users {user_id: {u_id}}), (ic:causes {cause_id: {c_id}) 
        CREATE (n)-[:SUPPORTS_CAUSE]->(ic)'''
        self.sess.run(query, u_id = user_id, c_id = cause_id)       
        
        return    
    
    def show_ngos_by_cause(self, cause_id):
        query = "MATCH (n:npo) WHERE n.ngo_cause_id = {c_id} RETURN n.ngo_cause_name LIMIT 10"
        self.sess.run(query, c_id = cause_id)
        return
    
    def show_ngos_nearme(self, city_id):
        query = "MATCH (n:npo) WHERE n.ngo_city_id = {c_id} RETURN n.ngo_cause_name LIMIT 10"
        self.sess.run(query, c_id = city_id)
        return    
    
    
    def show_events_nearme(self, city_id):

        query = "MATCH (n:events) WHERE n.event_city_id = {c_id} RETURN n.event_cause_name LIMIT 10"
        self.sess.run(query, c_id = city_id)

        
        return
    
    def show_ngos_recommended(self, user_id):
        
        query = '''MATCH (u:users {user_id: {u_id}})-[:SUPPORTS_CAUSE]->(c:causes)<-[:SUPPORTS_CAUSES]-(n:npo) 
        RETURN n.ngo_name LIMIT 10'''
        self.sess.run(query, u_id = user_id)
        
        return
    
    def show_events_recommended(self, user_id):
        
        query = '''MATCH (u:users {user_id: {u_id}})-[:SUPPORTS_CAUSE]->(c:causes)<-[:BELONGS_TO]-(e:events) 
        RETURN e.event_name LIMIT 10'''
        self.sess.run(query, u_id = user_id)
        
        return
        

    def show_issue_notif(self, issue_id, cause_id):
        return
        
    def show_updated_node(self, user_dict): 
        return

    
    def show_follow_corp_lnk(self,user_id, corp_id):
        return
    
    def show_support_issue_lnk(self,user_id, issue_id):
        return
    
    def show_create_issue_lnk(self,user_id, issue_id):
        return
    

    def show_follow_person_lnk(self, user_id, other_user_id):
        return
    
    def show_vol_ngo_lnk(self, user_id, ngo_id):
        return
    
    def show_attend_event_lnk(self, user_id, event_id):
        return
    
    def show_maybe_event_lnk(self, user_id, event_id):
        return
    

    def show_people_recommended(self, user_id):
        return
    
    def show_search_results(self, search_id ):
        return
        
# %%    
class NgoFeatures(object):
       
    def __init__(self):
        pass
    
    
    def create_profile(self, ngo):
        self.show_node(ngo.to_dict())
        self.show_cred_lnks(ngo.ref_id, ngo.city_id, ngo.cause_id)
        return
    
    def sign_in(self):
        return    
    
    def update_profile(self, ngo, name = None, lat = None, lon = None, city_id = None):
        
        if name:
            ngo.name = name        
        if lat:
            ngo.lot = lat 
        if lon:
            ngo.location = lon
        if city_id:
            ngo.city_id = city_id            
            
        self.show_updated_node(user.to_dict())
        
        return            
                   
    
    def search_by_id(self, ngo, search_id):
        self.show_search_results(search_id)
        return    
    
    def view_issue_suggestions(self, ngo):
        self.show_issues_recommended(ngo.ref_id)
        return
    
    def create_event(self,event):
        
        self.show_event_node(event.to_dict())
        self.show_create_event_lnk(event.ngo_id, event.ref_id)
        self.show_event_notif(event.ref_id, event.ngo_id, event.cause_id)
        return
# =============================================================================
#     visualization functions : Graph database
# =============================================================================
    def show_node(self, ngo_dict):  
        
        
        query = "CREATE (a:npo {ngo_name:{u_name}, ngo_id:{u_id}, ngo_lat:{u_lat}, ngo_lon:{u_lon}, ngo_city_id: {u_city_id}, ngo_cause_id: {u_cause_id}, ngo_city_name: {u_city_name}, ngo_cause_name: {u_cause_name}, ngo_state :{u_state}, ngo_zip: {u_zip}, ngo_link: {u_link}})"
        self.sess.run(query, u_name= ngo_dict['ngo_name'] , u_id = ngo_dict['ngo_id'], 
                      u_lat = ngo_dict['ngo_lat'], u_lon = ngo_dict['ngo_lon'],
                      u_city_id = ngo_dict['ngo_city_id'], 
                      u_cause_id = ngo_dict['ngo_cause_id'],
                      u_city_name = ngo_dict['ngo_city_name'], 
                      u_cause_name = ngo_dict['ngo_cause_name'],
                      u_state = ngo_dict['ngo_state'],
                      u_zip = ngo_dict['ngo_zip'],
                      u_link = ngo_dict['ngo_link'])
        
        print("ngo node created with attributes in the graph database")

        return
    
    def show_cred_lnks(self, ngo_id, city_id, cause_id):
        
        #ngo-city
        query = '''OPTIONAL MATCH (n:npo {ngo_id: {u_id}}), (ic:cities {city_id: {ci_id}) 
        CREATE (n)-[:LOCATED_IN]->(ic)'''
        self.sess.run(query, u_id = ngo_id, ci_id = city_id)

        #ngo-cause
        query = '''OPTIONAL MATCH (n:npo {ngo_id: {u_id}}), (ic:causes {cause_id: {co_id}) 
        CREATE (n)-[:SUPPORTS_CAUSE]->(ic)'''
        self.sess.run(query, u_id = ngo_id, co_id = cause_id)
        
  
        return
    
    
    def show_event_node(self, event_dict):
        
        query = "CREATE (a:events {event_name:{u_name}, event_id:{u_id}, event_lat:{u_lat}, event_lon:{u_lon}, event_city_id: {u_city_id}, event_cause_id: {u_cause_id}, event_city_name: {u_city_name}, event_cause_name: {u_cause_name}, event_state :{u_state}, event_zip: {u_zip}})"
        self.sess.run(query, u_name= event_dict['event_name'] , u_id = event_dict['event_id'], 
                      u_lat = event_dict['event_lat'], u_lon = event_dict['event_lon'],
                      u_city_id = event_dict['event_city_id'], 
                      u_cause_id = event_dict['event_cause_id'],
                      u_city_name = event_dict['event_city_name'], 
                      u_cause_name = event_dict['event_cause_name'],
                      u_state = event_dict['event_state'],
                      u_zip = event_dict['event_zip'])
        
        print("event node created with attributes in the graph database")

    
        return

    def show_issues_recommended(self, ngo_id):

        query = '''MATCH (n:npo {ngo_id: {u_id}})-[:SUPPORTS_CAUSE]->(c:causes)<-[:BELONGS_TO]-(i:issues) 
        RETURN i.issue_name LIMIT 10'''
        self.sess.run(query, u_id = ngo_id)        
        
        return
    
    
    def show_create_event_lnk(self, ngo_id, event_id):   
        
        #ngo-event
        query = '''OPTIONAL MATCH (n:npo {ngo_id: {u_id}}), (ic:events {event_id: {c_id}) 
        CREATE (n)-[:ORGANIZED]->(ic)'''
        
        self.sess.run(query, u_id = ngo_id, c_id = event_id)
        
        return
    
    def show_event_notif(self, event_id, ngo_id, cause_id):
        return
        
    def show_updated_node(self, ngo_dict):        
        return    
    
    def show_search_results(self, search_id ):
        return
        
# %%

class CorpFeatures(object):

    def __init__(self):
        pass

    def create_profile(self, corp):
        self.show_node(corp.to_dict())
        self.show_cred_lnks(corp.ref_id, corp.city_id, corp.cause_id)
        return 
    
    def sign_in(self):
        return    
    
    def update_profile(self, corp, name = None,  city_id = None):
        
        if name:
            corp.name = name                
        if city_id:
            corp.city_id = city_id        
            
        self.show_updated_node(corp.to_dict())        
        return

    def select_cause(self, corp, cause_id):
        corp.list_cause_ids.append(cause_id)
        self.show_liked_cause(corp.ref_id, cause_id)
        return
    
    def ngo_suggestions(self, corp):
        self.show_ngos_recommended(corp.ref_id)
        return corp.to_dict() 
    
    def search_ngos_nearme(self, corp):
        self.show_ngos_nearme(corp.city_id)
        return    
    
    def search_ngos_by_cause(self, corp, cause_id):
        self.show_ngos_by_cause(cause_id)
        return 
    
    def sponsor_ngo(self , corp, ngo_id):       
        corp.list_sponsor_ngo_ids.append(ngo_id)
        self.show_sponsor_ngo_lnk(corp.ref_id , ngo_id)
        return

    def follow_ngo(self , corp, ngo_id):       
        corp.list_follow_ngo_ids.append(ngo_id)
        self.show_follow_ngo_lnk(corp.ref_id , ngo_id)
        return
    
    def search_by_id(self, corp, search_id):
        self.show_search_results(search_id)
        return 
    
    
# =============================================================================
#     visualization functions : Graph database
# =============================================================================
    def show_node(self, corp_dict):  
        
        query = "CREATE (a:corporate_sponsors {corporate_name:{u_name}, corporate_id:{u_id}, corporate_lat:{u_lat}, corporate_lon:{u_lon}, corporate_city_id: {u_city_id}, corporate_cause_id: {u_cause_id}, corporate_city_name: {u_city_name}, corporate_cause_name: {u_cause_name}, corporate_state :{u_state}, corporate_zip: {u_zip}})"
        self.sess.run(query, u_name= corp_dict['corporate_name'] , u_id = corp_dict['corporate_id'], 
                      u_lat = corp_dict['corporate_lat'], u_lon = corp_dict['corporate_lon'],
                      u_city_id = corp_dict['corporate_city_id'], 
                      u_cause_id = corp_dict['corporate_cause_id'],
                      u_city_name = corp_dict['corporate_city_name'], 
                      u_cause_name = corp_dict['corporate_cause_name'],
                      u_state = corp_dict['corporate_state'],
                      u_zip = corp_dict['corporate_zip'])
        
        print("corporate node created with attributes in the graph database")
               
        return
    
    
    def show_cred_lnks(self, corp_id, city_id, cause_id):
        
        #corp-city
        query = '''OPTIONAL MATCH (n:corporate_sponsors {corporate_id: {u_id}}), (ic:cities {city_id: {ci_id}) 
        CREATE (n)-[:LOCATED_IN]->(ic)'''
        self.sess.run(query, u_id = corp_id, ci_id = city_id)

        #corp-cause
        query = '''OPTIONAL MATCH (n:corporate_sponsors {corporate_sponsors: {u_id}}), (ic:causes {cause_id: {co_id}) 
        CREATE (n)-[:SUPPORTS_CAUSE]->(ic)'''
        self.sess.run(query, u_id = corp_id, co_id = cause_id)
 
        return
    
    
    def show_follow_ngo_lnk(self,corp_id, ngo_id):
        
        #corp-ngo
        query = '''OPTIONAL MATCH (n:corporate_sponsors {corporate_id: {u_id}}), (ic:npo {ngo_id: {c_id}) 
        CREATE (n)-[:RELATED_TO]->(ic)'''
        
        self.sess.run(query, u_id = corp_id, c_id = ngo_id)

        return

    def show_ngos_by_cause(self, cause_id):
        query = "MATCH (n:npo) WHERE n.ngo_cause_id = {c_id} RETURN n.ngo_cause_name LIMIT 10"
        self.sess.run(query, c_id = cause_id)
        return
    
    def show_ngos_nearme(self, city_id):
        query = "MATCH (n:npo) WHERE n.ngo_city_id = {c_id} RETURN n.ngo_cause_name LIMIT 10"
        self.sess.run(query, c_id = city_id)
        return  
    
    def show_liked_causes(self, user_id, causes_list):

        return  
    
    def show_sponsor_ngo_lnk(self, user_id, ngo_id):
        
        return
    
    
    def show_ngos_recommended(self, corp_id):
        return
    
    def show_search_results(self, search_id ):
        return

    def show_updated_node(self, corp_dict):        
        return


