# 3 Little Pigs

## Introduction
Everyone knows the story of the 3 little pigs. But this is a little different. Instead of just reading the story you get to chose what happens. It's a choose your own adventure story of the 3 Little Pigs.

***

## How to play

To run the program and write your story. Clone the repo. Install required packages: SQLAlchemy and ipdb

```
pipenv install
pipenv shell
python lib/cli.py 

```

You will be taken to the beginning of the story where you choose your character and then your neighbor.

To write the story follow the prompts on the screen. If you decide you don't like where the story is going you can go back and make a different choice. But that will be rewriting your story. You can also go ahead with the story and see where it leads, save it. Then try again.

## Future releases

- option to be one of the wolves
- more grpahics

## Nitty Gritty
This program uses Pipenv, SQLAlchemy, Alembic, Python.

# Character Table
| Column | Type |
|-----|-----|
| id | Integer Primary Key|
| name | String |
| description | String |

# Scenes Table
| Column | Type |
|-----|-----|
| id | Integer Primary Key|
| scene_num | Integer |
| description | String |
| choiceA | String |
| choiceB | String

# Story Table
| Column | Type |
|-----|-----|
| id | Integer Primary Key|
| title | String |
| hero_id | Integer Foreign Key |
| antagonist_id | Integer Foreign Key |

# Storyline Table
| Column | Type |
|-----|-----|
| id | Integer Primary Key|
| story_id | Integer Foreign Key |
| scene_key | Integer Foreign Key |

## Maintainer

- Alyssa Essman - [Linkedin](https://www.linkedin.com/in/alyssa-essman/)


# Additional Resources

-websites used 