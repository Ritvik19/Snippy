printf "%.0f
" 123.456 # 123
printf "%.0f
" 7.89    # 8

echo 123.456 | awk '{print int($1)}' # 123
echo 7.89 | awk '{print int($1)}'    # 7

echo 123.456 | awk '{print ($0-int($0)<0.499)?int($0):int($0)+1}' # 123
echo 7.89 | awk '{print ($0-int($0)<0.499)?int($0):int($0)+1}'    # 8

# floor
echo 1.23 | awk '{print int($0)}'                          # 1
# ceil
echo 1.23 | awk '{print ($0-int($0)>0)?int($0)+1:int($0)}' # 2