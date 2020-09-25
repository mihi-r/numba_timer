from numba import cuda

class Timer:
    """A timer to measure CUDA computation time."""
    def __init__(self):
        self._start = cuda.event(timing=True)
        self._stop = cuda.event(timing=True)

    def start(self):
        """Start the timer."""
        self._start.record(0)
    
    def stop(self):
        """Stop the timer."""
        self._stop.record(0)
    
    def elapsed(self):
        """Get the elapsed time between the last start and stop in milliseconds.

        Returns:
            A float time in milliseconds.
        """
        self._stop.synchronize()
        return cuda.event_elapsed_time(self._start, self._stop)

    def elapsed_seconds(self):
        """Get the elapsed time between the last start and stop in seconds.

        Returns:
            A float time in seconds.
        """
        return self.elapsed() / 1000
