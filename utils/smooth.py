import numpy as np
from scipy.signal import savgol_filter

def smooth(u: np.ndarray, F: np.ndarray, window_size: int) -> tuple[np.ndarray, np.ndarray]:
    """Smooth a force sequence using Savitzky–Golay filtering on monotonic segments.

    The curve is split at local extrema detected in the displacement sequence `u`
    (where consecutive slope signs change). Each segment of `F` is smoothed
    independently with a Savitzky–Golay filter using the provided `window_size`.

    Args:
        u (np.ndarray): Displacement sequence.
        F (np.ndarray): Force sequence.
        window_size (int): Window size (will be adjusted to a valid odd length per segment).

    Returns:
        tuple[np.ndarray, np.ndarray]: (original force sequence, smoothed force sequence)
    """
    i0 = 0
    F_new = F.copy()
    for i in range(1, len(u) - 1):
        if (u[i + 1] - u[i]) * (u[i] - u[i - 1]) < 0:
            F_seg = F[i0: i + 1]
            F_seg_new = _SMA(F_seg, window_size)  # now Savitzky–Golay under the hood
            F_new[i0: i + 1] = F_seg_new
            i0 = i
    F_new[i0:] = _SMA(F[i0:], window_size)
    return F, F_new


def _SMA(data: np.ndarray, window_size: int) -> list[float]:
    """Savitzky–Golay smoothing (compatibility wrapper).

    This replaces the former simple moving average with a Savitzky–Golay filter.
    The window length is coerced per segment to a valid odd integer ≤ len(data).
    For very short segments (length < 3) no smoothing is applied.

    Args:
        data (np.ndarray): Data segment to smooth.
        window_size (int): Desired window size.

    Returns:
        list[float]: Smoothed data (same length as `data`).
    """
    n = len(data)
    if n < 3:
        # Not enough points for SG with polyorder ≥ 2; return as-is.
        return data.tolist()

    # Ensure a valid odd window length no larger than the segment
    win = max(3, window_size)
    if win % 2 == 0:
        win -= 1  # prefer nearest lower odd to stay ≤ n
    if win > n:
        # Reduce to the largest valid odd ≤ n
        win = n if n % 2 == 1 else n - 1
        if win < 3:
            return data.tolist()

    # Choose a safe polynomial order (< window length)
    polyorder = min(3, win - 1)

    # Apply SG; use mode='nearest' to handle edges robustly per segment
    smoothed = savgol_filter(data, window_length=win, polyorder=polyorder, mode='nearest')
    return smoothed.tolist()
