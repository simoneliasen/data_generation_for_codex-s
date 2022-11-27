class Data:

    def __init__(self, data_dir="Codex-s/", reverse=False):
        self.train_data = self.load_data(data_dir, "train", reverse=reverse)
        self.valid_data = self.load_data(data_dir, "valid", reverse=reverse)
        self.test_data = self.load_data(data_dir, "test", reverse=reverse)
        self.data = self.train_data + self.valid_data + self.test_data
        self.entities = self.get_entities(self.data)
        self.train_relations = self.get_relations(self.train_data)
        self.valid_relations = self.get_relations(self.valid_data)
        self.test_relations = self.get_relations(self.test_data)
        self.relations = self.train_relations + [i for i in self.valid_relations \
                if i not in self.train_relations] + [i for i in self.test_relations \
                if i not in self.train_relations]

    def load_data(self, data_dir, data_type="train", reverse=False):
        with open("%s%s.txt" % (data_dir, data_type), "r") as f:
            data = f.read().strip().split("\n")
            data = [i.split() for i in data]
            if reverse:
                data += [[i[2], i[1]+"_reverse", i[0]] for i in data]
        return data

    def get_relations(self, data):
        relations = sorted(list(set([d[1] for d in data])))
        return relations

    def get_entities(self, data):
        entities = sorted(list(set([d[0] for d in data]+[d[2] for d in data])))
        return entities



DataObject = Data(data_dir="Codex-s/", reverse=False)


relations = DataObject.relations
entities = DataObject.entities


relationdict = { i : relations[i] for i in range(0, len(relations) ) }
f = open("Codex-s/relations.dict", "w")
for k in relationdict.keys():
    f.write("{}'{}\n".format(k, relationdict[k]))
f.close()

entitydict = { i : entities[i] for i in range(0, len(entities) ) }
f = open("Codex-s/entities.dict", "w")
for k in entitydict.keys():
    f.write("{}'{}\n".format(k, entitydict[k]))
f.close()

entity2iddict = { i : entities[i] for i in range(0, len(entities) ) }
f = open("Codex-s/entity2id.txt", "w")
for k in entity2iddict.keys():
    f.write("{}'{}\n".format(entity2iddict[k], k))
f.close()

relation2iddict = { i : entities[i] for i in range(0, len(entities) ) }
f = open("Codex-s/relation2id.txt", "w")
for k in relation2iddict.keys():
    f.write("{}'{}\n".format(relation2iddict[k], k))
f.close()