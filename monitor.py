class Monitor:
    cache_access_time = 0.5  # Example access time in nanoseconds
    memory_access_time = 100  # Example access time in nanoseconds
    
    def __init__(self):
        self.cache_misses = 0
        self.cache_hits = 0
        self.cache_accesses = 0
        self.memory_accesses = 0

    def record_cache_hit(self):
        self.cache_hits += 1

    def record_cache_miss(self):
        self.cache_misses += 1

    def record_cache_access(self):
        self.cache_accesses += 1

    def record_memory_access(self):
        self.memory_accesses += 1
    
    def get_total_time(self):
        return (self.cache_accesses * Monitor.cache_access_time) + (self.memory_accesses * Monitor.memory_access_time)
    