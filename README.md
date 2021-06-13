# project-sme-impact
Hackbright capstone project. 
# Foobar

Foobar is a Python library for dealing with word pluralization.

## Description

Technical training teams consult with software engineers and product managers as subject matter experts (SMEs) to develop on-demand training lessons. These lessons are deployed via a Learning Management System (LMS) from the vendor Skilljar. This LMS does not have a feature to track which SMEs correlate to lessons. My goal was to develop a simple site where technical trainers (the users) can look up, add, or delete a SME, then via an API call, bring back the name of a lesson and the number of enrollments it has had. This data is useful when looping back with SMEs to advise them on the impact of their trainings and to encourage them to co-create more lessons.


```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)