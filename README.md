# 3 Little Pigs


https://github.com/arbitrary-berry/3_little_pigs/assets/128105913/b99de5d1-549a-42ee-a4b5-ae204f73e8e4

## Introduction
Everyone knows the story of the 3 little pigs. But this is a little different. Instead of just reading the story you get to choose what happens. It's a choose-your-own-adventure story of the 3 Little Pigs.

***

## How to play

To run the program and write your story: Clone the repo. Install the required packages: SQLAlchemy and ipdb

```
pipenv install
pipenv shell
python lib/cli.py 

```

You will be taken to the beginning of the story where you choose your character and then your neighbor.

Follow the prompts on the screen. If you decide you don't like where the story is going you can go back and make a different choice. But that will be rewriting your story. You can also go ahead with the story and see where it leads, save it. Then try again.

## Future releases

- option to:
    - choose to be one of the wolves
    - add a title at the end of the story
- more graphics for each scene, some choices are commented out in cli.py
- have the ending more complete
- format text of printed description


## Nitty Gritty
This program uses Pipenv, SQLAlchemy, Alembic, Python.

## Story Flow - Functions

cli.py:
function display_welcome(): displays the welcome message, 3 Little Pigs and an ascii image of the three houses and pigs.

function display_main_menu(): Prints the beginning of the story and your choices of which pig you'd like to be: Albert, Brenda, or Charlie. Then handle_pig_choice() takes the input and saves the choice to the STORY table.

function choose_your_neighbor(): Prints an ascii image of a wolf and then you select who you want as your neighbor: THE Wolf or BB Wolf. Then handle_neighbor_choice() takes the input and saves the choice to the STORY table.

function set_up_story(): Takes the saved pig and wolf choice and depending on the selection shows the first scene, saving to the STORY table and STORYLINE table.

function display_current_scene(): Begins the story after the story set up and takes each following decision and shows the corresponding scene, and just loops through until it ends at THE END.

storyline.drawio:
This is the decision tree for all the potential storylines.

## Character Table
| Column | Type |
|-----|-----|
| id | Integer, Primary Key|
| name | String |
| description | String |

## Scenes Table
| Column | Type |
|-----|-----|
| id | Integer, Primary Key|
| scene_num | Integer |
| description | String |
| choiceA | String |
| choiceB | String

## Story Table
| Column | Type |
|-----|-----|
| id | Integer, Primary Key|
| title | String |
| hero_id | Integer, Foreign Key |
| antagonist_id | Integer, Foreign Key |

## Storyline Table
| Column | Type |
|-----|-----|
| id | Integer, Primary Key|
| story_id | Integer, Foreign Key |
| scene_key | Integer, Foreign Key |

## Maintainer

- Alyssa Essman - [Linkedin](https://www.linkedin.com/in/alyssa-essman/)


# Resources

- story book: "The True Story of the 3 Little Pigs" As told to Jon Scieszka, Illustrated by Lane Smith
- websites used:
    - [The Three Little Pigs](https://americanliterature.com/childrens-stories/the-three-little-pigs)
    - [All about the 3 Little Pigs](https://www.gutenberg.org/files/32504/32504-h/32504-h.htm)
    - [The Story of the 3 Little Pigs](https://www.gutenberg.org/files/18155/18155-h/18155-h.htm)
    - [ASCII Art Archive](https://www.asciiart.eu/)
    - [ASCII](https://ascii.co.uk/)
    - [Figma](https://www.figma.com/)
