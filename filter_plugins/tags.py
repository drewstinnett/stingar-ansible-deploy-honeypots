class FilterModule(object):
    def filters(self):
        return {
            'stingar_tags': self.stingar_tags
        }

    def stingar_tags(self, tags):
        remapped_entries = []
        for k, v in tags.items():
            remapped_entries.append('%s:%s' % (k, v))
        return ",".join(remapped_entries)
