import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = [Node(ch, freq) for ch, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def generate_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = current_code if current_code else "0"

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

    return codes

text = input("Enter text to encode: ")

if not text:
    print("Please enter some text.")
else:
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    root = build_huffman_tree(freq)
    codes = generate_codes(root)

    encoded_text = "".join(codes[ch] for ch in text)

    print("\nCharacter | Frequency | Huffman Code")
    print("------------------------------------")

    for ch in freq:
        print(f"    {ch!r}     |     {freq[ch]}      |    {codes[ch]}")

    print("\nEncoded Text:", encoded_text)