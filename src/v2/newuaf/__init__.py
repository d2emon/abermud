from ..gamego.error import MudError
from ..opensys import Service, WorldError


def bprintf(message):
    raise NotImplementedError()


def getkbd(max_length):
    raise NotImplementedError()


def pbfr():
    raise NotImplementedError()


class PersonService(Service):
    NAME = 'UAF_RAND'
    __data = {}

    def __init__(self):
        try:
            super().__init__(read=True, create=True)
        except WorldError:
            raise MudError("Cannot access UAF")

    @property
    def data(self):
        return self.__data

    def find(self, person_id):
        person = self.data.get(person_id)
        self.disconnect()
        return person

    def create(self, person):
        try:
            self.write(person.person_id, person)
        except WorldError:
            bprintf("Save Failed - Device Full?")
        finally:
            self.disconnect()


class Person:
    size = 32

    def __init__(self, person_id, score=0, strength=40, sex=0, level=1):
        self.person_id = person_id
        self.score = score
        self.strength = strength
        self.sex = sex
        self.level = level

    @classmethod
    def find(cls, person_id):
        return PersonService().find(person_id) is not None

    @classmethod
    def create(cls, person_id, score=0, strength=40, sex=0, level=1):
        person = cls(
            person_id,
            score=score,
            strength=strength,
            sex=sex,
            level=level,
        )
        PersonService().create(person)
        return person


def delpers(person_id):
    service = PersonService()
    person = service.find(person_id)
    if person is None:
        return

    person_id = person_id.lower()
    if person.person_id.lower() != person_id:
        raise MudError("Panic: Invalid Persona Delete")
    person.name = ""
    person.level = -1
    service.write(person.person_id, person)
    service.disconnect()
    return delpers(person_id)


def new_person(person_id):
    def get_sex():
        bprintf("\nSex (M/F) : ")
        pbfr()
        s = getkbd(2).lower()[0]
        if s == 'm':
            return 0
        elif s == 'f':
            return 1
        else:
            bprintf("M or F")
            get_sex()

    try:
        person = Person.find(person_id)
    except FileNotFoundError:
        raise MudError("Panic: Timeout event on user file")

    if person is None:
        bprintf("Creating character....")
        return Person.create(person_id, sex=get_sex())
    return person


def saveme(player):
    if player.zapped:
        return

    bprintf("\nSaving {}\n".format(player.name))
    return Person.create(
        player.person.person_id,
        strength=player.person.strength,
        level=player.person.level,
        sex=player.data.sexall,
        score=player.person.score,
    )


"""
 validname(name)
 char *name;
    {
    long a;
    if(resword(name)){bprintf("Sorry I cant call you that\n");return(0);  }
    if(strlen(name)>10)
       {
       return(0);
       }
    a=0;
    while(name[a])
       {
       if(name[a]==' ')
          {
          return(0);
          }
       a++;
       }
    if(fobn(name)!=-1)
       {
      bprintf("I can't call you that , It would be confused with an object\n");
       return(0);
       }
    return(1);
    }
 
resword(name)
{
if(!strcmp(name,"The")) return(1);
if(!strcmp(name,"Me")) return(1);
if(!strcmp(name,"Myself")) return(1);
if(!strcmp(name,"It")) return(1);
if(!strcmp(name,"Them")) return(1);
if(!strcmp(name,"Him")) return(1);
if(!strcmp(name,"Her")) return(1);
if(!strcmp(name,"Someone")) return(1);
return(0);
}
"""
