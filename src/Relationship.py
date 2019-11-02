class Relationship:
    def __init__(self, name, relationshipvalue, relationshipstring, relationshiptype, status):
        self.name = name
        self.relationshipvalue = relationshipvalue
        self.relationshipstring = relationshipstring
        self.relationshiptype = relationshiptype
        self.status = status

    def calculateRelationship(self):
        #Set 0 and 100 boundary
        if self.relationshipvalue < 0:
            self.relationshipvalue = 0
        if self.relationshipvalue > 100:
            self.relationshipvalue = 100

        #Set criteria for relationship 'gates'
        if self.relationshipvalue < 25:
            self.relationshipstring = "Poor"
        elif self.relationshipvalue > 25 and self.relationshipvalue < 50:
            self.relationshipstring = "Moderate"
        elif self.relationshipvalue > 50 and self.relationshipvalue < 75:
            self.relationshipstring = "Good"
        elif self.relationshipvalue > 75 and self.relationshipvalue >= 100:
            self.relationshipvalue = "Excellent"