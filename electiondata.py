class ElectionResults:
  
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    self.file = open(self.filename, 'r')
    self.all_lines = self.file.readlines()

  def states(self):
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      all_names.append(columns[1])
    return all_names

  def state_count(self):
    return len(self.all_lines)
  
  def get_votes(self,candidate):
    if candidate=="obama":
      column_index=3
    else:
      column_index=5
    vote_count = 0
    for idx, line in enumerate(self.all_lines):
      columns = line.split(',')
      if idx > 0:
        vote_count=vote_count+int(columns[column_index])
    return vote_count