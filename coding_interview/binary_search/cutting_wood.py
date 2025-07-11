from typing import List

def cutting_wood(heights: List[int], k: int) -> int:
    max_height = max(heights)
    
    left, right = 0, max_height
    
    def get_total_cut(cut: int):
        total_cut = 0
        for h in heights:
            # No cut is possible, since wood height is less than the cut
            if h <= cut:
                continue
            # Total cut has to be at least k, no need to continue
            if total_cut > k:
                break
            total_cut += h - cut
        return total_cut
    
    while left < right:
        # We are looking for the Upper bound, and preventing inifinite loop - the heighest possible H that cut at least k-woods lenghts
        mid = (left + right) // 2 + 1
        print(f"===LEFT={left}, RIGHT={right}, MID={mid}===")
        
        total_mid_cut = get_total_cut(mid)
        
        print(f"total mid cut = {total_mid_cut} at H={mid}")
        display_histogram_with_height(heights, mid)
        
        # H is too high, We need to cut more, so the H needs to be lower
        if total_mid_cut < k:
            right = mid - 1
        
        # H is too low, we can try to cut less, so H can be higher
        if total_mid_cut >= k:
            left = mid
            
    return left


def display_histogram_with_height(heights, H):
    max_height = max(max(heights), H)
    width = len(heights)

    # Build the display from top down
    for row in range(max_height, -1, -1):
        line = ""
        for h in heights:
            if h > row:
                if row >= H:
                    line += "░ "  # Patterned block above H
                else:
                    line += "█ "  # Solid block below H
            elif row == H:
                line += "─ "  # H line
            else:
                line += "  "  # Empty space
        # Y-axis label, explanation {row:>2} -> :starts the format sepcification, > right align, 2 is the minimum width of the field is 2 chars
        print(f"{row:>2} | {line}")

    # X-axis
    print("   +" + "--" * width)
    print("     " + " ".join(str(i) for i in range(width)))
    print(f"H = {H}")
    


if __name__ == "__main__":
    heights = [2, 6, 3, 8]
    result = cutting_wood(heights, k=0)
    print(result)
    