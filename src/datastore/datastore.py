import os
import abc
import time


class Transaction:
    class TransactionType:
        create = 'create'
        update = 'update'
        delete = 'delete'

    class ObjectType:
        user = 'user'
        project = 'project'
        column = 'column'
        task = 'task'

    def __init__(
            self,
            transaction_type : TransactionType,
            object_type : ObjectType,
            user_signature : str,
            timestamp : int,
            attributes : dict):
        self.transaction_type = transaction_type
        self.object_type = object_type
        self.user_signature = user_signature
        self.timestamp = timestamp
        self.attributes = attributes

    @classmethod
    def create(
            cls,
            transaction_type : TransactionType,
            object_type : ObjectType,
            user_signature : str,
            **kwargs):
        timestamp = time.time_ns()
        cls.__init__(
                cls,
                transaction_type,
                object_type,
                user_signature,
                timestamp,
                kwargs)

    def from_string(
            cls,
            string,

class TransactionGenerator(abc.ABC):
    @abc.abstractclassmethod
    def create_user(
            self,
            name : str,
            birthdate : str,
            signature : str,
            rights : str):
        pass

    def update_user(
            self,
            signature : str,
            name : str,
            birthdate : str,
            attribute_name : str,
            attribute_value : str):
        pass

    def delete_user(
            self,
            signature : str,
            naem : str,
            birthdate : str):
        pass

    def get_users_by_name(
            self,
            signature : str,
            name : str):
        pass

    def create_project(
            self,
            signature : str,
            name : str):
        pass

    def update_project(
            self,

class DataStore:
    def __init__(self,):
        if not os.path.exists(file_location):
