>>> stuff = {’name’: ’Zed’, ’age’: 39, ’height’: 6 * 12 + 2} >>> print stuff[’name’]
Zed
>>> print stuff[’age’]
39
>>> print stuff[’height’]
74
>>> stuff[’city’] = ”San Francisco”
>>> print stuff[’city’]
San Francisco
                                                                                           stuff                                                                                                                                    
                                        
￼>>> stuff[1] = ”Wow”
>>> stuff[2] = ”Neato”
>>> print stuff[1]
Wow
>>> print stuff[2]
Neato
>>> stuff
{’city’: ’San Francisco’, 2: ’Neato’, ’name’: ’Zed’, 1: ’Wow’, ’age’: 39, ’height’: 74}
