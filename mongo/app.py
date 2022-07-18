from attr import validate
from bson import ObjectId
from mongo.dbmongo import dbmongo
import hashlib
import jwt
import json


class Workbase():
    def __init__(self,obj):
        try:
            hash = hashlib.md5()
            hash.update(bytes(obj['password'], 'utf-8'))
        except:
            pass
        try:
            self.password = hash.hexdigest()
        except:
            pass
        try:
            self.project_id = obj['project_id']
        except:
            pass
        try:
            self.user_id = obj['user_id']
        except:
            pass
        try:
            self.started_at = obj['started_at']
        except:
            pass
        try:
            self.ended_at = obj['ended_at']
        except:
            pass
        try:
            self.login = obj['login']
        except:
            pass
        try:
            self.name = obj['name']
        except:
            pass
        try:    
            self.email = obj['email']
        except:
            pass
        try:
            self.description = obj['description']
        except:
            pass
        try:
            self.title = obj['title']
        except:
            pass
        try:
            self.time_id = obj['time_id']
        except:
            pass
        try:
            self.project_id = obj['project_id']
        except:
            pass
        try:
            self.started_at = obj['started_at']
        except:
            pass
        try:
            self.ended_at = obj['ended_at']
        except:
            pass
        try:
            self.currenttoken = obj['currenttoken']
        except:
            pass

    def creatuser(self):
        try:
            value = {'name':self.name,'email':self.email,'login':self.login,'password':self.password,"token":''}
            table = "users"
            query = {'login':value['login']}
            validate = dbmongo().select(table,query)
            if validate == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                value['password'] = 'registered'
                return {"user":value}, 201
            else:
                return  ({ "message" : 'User already existed' },404)
        except:
            return  ({ "message" : 'it was not possible to register User' },404)

    def validateuser(self):
        table = 'users'
        query = {'login':self.login}
        validatelogin = dbmongo().select(table,query)
        if validatelogin == [] or validatelogin[0]['password'] != self.password:
            return ({ "message" : 'This user has not yet been registered or the password is invalid' },404)
        else:
            payload = validatelogin[0]
            payload['password'] = 'registered'
            payload['_id'] = str(payload['_id'])
            key= '1234'
            encoded_jwt = jwt.encode(payload=payload, key=key, algorithm="HS256")
            js = {"_id":ObjectId(payload['_id'])}
            values= {"token":encoded_jwt}
            res = dbmongo().update_by_js(table, js, values)
            print(res)
            Success = { "token": encoded_jwt, "user": payload }
            return (Success,200)

    def validatetoken(self):
        try:
            table = 'users'
            query = {'token': self.currenttoken}
            validate = dbmongo().select_one(table,query)
            if validate['token'] == self.currenttoken:
                return { "token": 'valid'}
            else:
                return { "token": 'invalid'}
        except:
            return { "token": 'invalid'}

    def idselectuser(self):
        try:
            table = "users"
            js = {"_id":ObjectId(self.user_id)}
            validate = dbmongo().select(table, js)
            print(validate)
            if validate == []:
                return ({ "message" : 'User not registered' },404)
            else:
                validate = validate[0]
                value = { 'name':validate['name'],'email':validate['email'],'login':validate['login'] }
                return ({"user": value}, 201)
        except:
            return ({ "message" : 'Unable to query user' }, 404)

    def putuser(self):
        try:
            table = "users"
            values = {'name':self.name,'email':self.email,'login':self.login,'password':self.password}
            js = {"_id":ObjectId(self.user_id)}
            dbmongo().update_by_js(table, js, values)
            user = dbmongo().select_one(table, js)
            user['_id'] = str(user['_id'])
            if user == []:
                return ({'message':f"User do'nt exist, register it using another location"},404)
            else:
                return ({'user':user},201)
            
        except:
            return ({'message':f"could not find the project id"},404)
        
    def createproject(self):
        try:
            table="projects"
            value = {"title":self.title,"description":self.description,"user_id":self.user_id}
            query = {'title':self.title}
            validate = dbmongo().select(table,query)
            if validate == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                return {"user":value},201
            else:
                return ({'message':f"item already exists, overwrite using another location"},404)
        except:
            return ({'message':f"don't cold created inten"},404)

    def selectprojects(self):
        try:
            table="projects"
            validate = dbmongo().select(table)
            validate=list(validate)
            for i in validate:
                i['_id'] = str(i['_id'])
            return ({"user":validate},201)
        except:
            return ({'message':f"don't cold load projects"},404)

    def selectprojectid(self):
        try:
            table = "projects"
            js = {"_id":ObjectId(self.project_id)}
            validate = dbmongo().select(table, js)
            print(validate)
            if validate == []:
                return ({ "message" : 'User not registered' },404)
            else:
                validate = validate[0]
                validate['_id'] = str(validate['_id'])
                return ({"user": validate}, 201)
        except:
            return ({ "message" : 'Unable to query time' }, 404)

    
    def putproject(self):
        try:
            table = "projects"
            values = {"title":self.title,"description":self.description, "user_id":self.user_id}
            js = {"_id":ObjectId(self.project_id)}
            dbmongo().update_by_js(table, js, values)
            project = dbmongo().select_one(table, js)
            project['_id'] = str(project['_id'])
            if project == []:
                return ({'message':f"could not find the project id"}, 404)
            else:
                return ({'project':project},201)
        except:
            return ({'message':f"could not find the project id"},404)

    def idselecttime(self):
        try:
            table = "times"
            js = {"_id":ObjectId(self.time_id)}
            validate = dbmongo().select(table, js)
            print(validate)
            if validate == []:
                return ({ "message" : 'User not registered' },404)
            else:
                validate = validate[0]
                validate['_id'] = str(validate['_id'])
                return ({"user": validate}, 201)
        except:
            return ({ "message" : 'Unable to query time' }, 404)
    
    def registertime(self):
        try:
            table="times"
            value ={ "project_id": str(self.project_id), "user_id": str(self.user_id), "started_at": str(self.started_at), "ended_at": str(self.ended_at) }
            query = {'project_id':self.project_id}
            validateid = dbmongo().select(table,query)
            print(validateid)
            query = {'user_id':value['user_id']}
            validateuser = dbmongo().select(table,query)
            print(validateuser)
            if validateid == [] or validateuser == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                return ({"user":value},201)
            else:
                return ({ "message" : 'Time has already been recorded. To change the recorded time please use another location.' }, 201)
        except:
                return ({ "message" : 'It was not possible to register time' }, 404)
    
    def puttime(self):
        try:
            table='times'
            values = { "project_id": str(self.project_id), "user_id": str(self.user_id), "ended_at": str(self.ended_at) } 
            query = {'project_id':self.project_id}
            validateid = dbmongo().select(table,query)
            print(validateid)
            query = {'user_id':values['user_id']}
            validateuser = dbmongo().select(table,query)
            print(validateuser)
            if validateid != [] or validateuser != []:
                js = {"_id":ObjectId(self.time_id)}
                dbmongo().update_by_js(table, js, values)
                time = dbmongo().select_one(table, js)
                time['_id'] = str(time['_id'])
                return ({'time':time},201)
        except:
            return ({'message':f"could not find the time"},404)