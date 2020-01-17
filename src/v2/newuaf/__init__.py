from ..gamego.error import MudError


def bprintf(message):
    raise NotImplementedError()


def getkbd(max_length):
    raise NotImplementedError()


def pbfr():
    raise NotImplementedError()


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

    def create(self):
        PersonService().create(self)


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


class PersonService:
    __FILENAME = 'UAF_RAND'

    def __init__(self):
        try:
            self.data = self.connect(self.__FILENAME, read=True, create=True)
        except FileNotFoundError:
            raise MudError("Cannot access UAF")

    @classmethod
    def connect(cls, name, **kwargs):
        raise NotImplementedError()

    def disconnect(self):
        raise NotImplementedError()

    def read(self, size):
        raise NotImplementedError()

    def write(self, person_id, person):
        raise NotImplementedError()

    def __get_person(self):
        try:
            yield self.read(Person.size)
        except MudError:
            return None

    def __find(self, person_id):
        return next((person for person in self.__get_person() if person.person_id.lower() == person_id), None)

    def find(self, person_id):
        person = self.__find(person_id)
        self.disconnect()
        return person

    def create(self, person):
        record = self.__find(person.person_id) or self.__find("")
        if record is not None:
            person_id = record.person_id
        else:
            self.data = self.connect(self.__FILENAME, append=True)
            person_id = person.person_id

        try:
            self.write(person_id, person)
        except MudError:
            bprintf("Save Failed - Device Full?")

        self.disconnect()


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
        person = Person(person_id, sex=get_sex())
        person.create()
    return person


def saveme(player):
    person = Person(player.person.person_id)
    person.strength = player.person.strength
    person.level = player.person.level
    person.sex = player.data.sexall
    person.score = player.person.score

    if player.zapped:
        return

    bprintf("\nSaving {}\n".format(player.name))
    person.create(player.person.person_id)


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
