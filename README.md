# AnalysingOfCompressionAlgorithms
Analysing of some lossless data compression algorithms 

## Usage 
* run ```python [average] <dir1> <dir2> <dir3>``` where _dirs_ are directories in __FILES__ folder. 
* Use ```average``` option to analyse files by directory.
## Output
Program outputs a csv table in __CSV__ folder and bar charts in __PLOTS__ folder.
### Example CSV output for various source code files (js/py/c#)

|   | Алгоритм | Размер до | Размер после | Отношение сжатия | Процент сжатия | Время сжатия | Время распаковки | Кол-во запусков функций | 
|---|----------|-----------|--------------|------------------|----------------|--------------|------------------|-------------------------| 
| 0 | RLE      | 23533.0   | 20013.0      | 0.886            | 11.42          | 0.0034       | 0.0004           | 1                       | 
| 1 | Huffman  | 23533.0   | 13585.0      | 0.682            | 31.8           | 0.0048       | 0.0007           | 1                       | 
| 2 | LZMA     | 23533.0   | 4574.0       | 0.345            | 65.51          | 0.0318       | 0.0017           | 1                       | 
| 3 | DEFLATE  | 23533.0   | 4965.0       | 0.32             | 67.97          | 0.0039       | 0.0005           | 1                       | 
