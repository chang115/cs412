from django.db import models
from datetime import datetime

class Voter(models.Model):

    last_name = models.TextField()
    first_name = models.TextField()
    street_number = models.TextField()
    street_name = models.TextField()
    apartment_number = models.CharField(max_length=100, null=True, blank=True) 
    zip_code = models.TextField()
    date_of_birth = models.DateField()
    date_of_registration = models.DateField()
    party_affiliation = models.TextField()
    precinct_number = models.TextField()
    
    # Recent election participation
    v20state = models.BooleanField(default=False)
    v21town = models.BooleanField(default=False)
    v21primary = models.BooleanField(default=False)
    v22general = models.BooleanField(default=False)
    v23town = models.BooleanField(default=False)
    voter_score = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
def load_data():

    Voter.objects.all().delete()

    filename = '/Users/ebow1/OneDrive/Documents/CS412/newton_voters.csv'
    f = open(filename)
    f.readline() 

    for line in f:

        # line = f.readline().strip()
        fields = line.split(',')
        
        try:
            voter = Voter(last_name=fields[1],
                          first_name=fields[2],
                          street_number=fields[3],
                          street_name=fields[4],
                          apartment_number=fields[5],
                          zip_code=fields[6],
                          date_of_birth=datetime.strptime(fields[7], "%Y-%m-%d").date(),
                          date_of_registration=datetime.strptime(fields[8], "%Y-%m-%d").date(),
                          party_affiliation=fields[9].strip(),
                          precinct_number=fields[10],
                         
                          v20state=True if fields[11] == 'TRUE' else False,
                          v21town=True if fields[12] == 'TRUE' else False,
                          v21primary=True if fields[13] == 'TRUE' else False,
                          v22general=True if fields[14] == 'TRUE' else False,
                          v23town=True if fields[15] == 'TRUE' else False,
                          voter_score=int(fields[16]),
                         ) 
            
            voter.save()
            print(f'Created voter: {voter}')
        
        except:
            print(f"Skipped: {fields}")
    print(f'Done. Created {len(Voter.objects.all())} Voters.')