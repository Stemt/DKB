# DKB DataStore file format

This document describes the file format used by the datastore module.

The current file format version is '0.1.0'

In general the data is stored as plain text and consists as discrete create, delete and update operations.

note that all fields indicated using curly braces ('{' and '}') are all seperated by atleast one space and no other charachters unless specified otherwise.


## Header

The at the top of the file the header is located which contains the following string
```
DKB_DS {version} {timestamp}
```
where '{version}' is replaced with the current file format version at the time of creation
and '{date}' is replaced with the date at the time of creation in ISO format (YYYY-MM-DD)

## body

On subsequent lines after the header the body is located.
The body consists of so called 'operations' each of which indicate a change of the data inside of the DataStore.
Each operation takes up a single line.

An operation is formatted as follows:
```
{operation_type} {user_signature} {timestamp}:{object_type} {attribute_pairs}
```

where '{operation_type}' can be either 'create', 'update' or 'delete'
and '{user_signature}' is replaced with the signature of the user (generated from a username and password
and '{timestamp}' is replaced with a unix timestamp in nanoseconds
and '{object_type}' can be either 'user', 'project', 'column' or 'task'
and '{attribute_pairs}' are a combination of an attribute names and values formatted as

```
{attribute_name}={attribute_value}
```
As you can see the fields here in this case are not seperated by a space but by a '='.

'{attribute_name}' and '{attribute_value}' should both be replaced with strings beginning and ending with quotes ".

e.g.
```
"name"="Jerry"
```

## Objects

Each object_type has its own attributes of which some are optional and others are not.
See the following table for an overview.

| object_type | attribute          | optional | Description                                                                                                                |
| ----------- | ------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| user        | name               | no       | human readable name for the user                                                                                           |
|             | birthdate          | no       | this field is here to decrease the likelyhood that a conflict will occur when two users use the same username and password |
|             | signature          | no       | hash generated from a combination of the username, birthdate and password                                                  |
|             | rights             | no       | strings indicating the rights of the user                                                                                  |
| project     | name               | no       | human readable name for a project                                                                                          |
|             | uuid               | no       | universally unique id for the project                                                                                      |
|             | user_signature     | no       | signature of user who created the project                                                                                  |
| column      | name               | no       | Human readable name of the column, must be unique inside of a project                                                      |
|             | project_uuid       | no       | uuid of the associated project                                                                                             |
| task        | name               | no       | human readable name of the task, must be unique inside of a project                                                        |
|             | column_name        | no       | name of a column                                                                                                           |
|             | description        | yes      | description of task                                                                                                        |
|             | deadline_timestamp | yes      | unix timestamp for a deadline of the task                                                                                  |
|             | time_estimate      | yes      | a time estimate in minutes                                                                                                 |

## User rights

| letter | description                                                                                              |
| ------ | -------------------------------------------------------------------------------------------------------- |
| a      | admin rights allows the user to do everything possible. This right can only be changed by another admin. |
| u      | gives user the right to create and ascribe rights to other users                                         |
| w      | gives the user the right to create new objects                                                           |
| r      | gives the user the right to view objects from the database                                               |
