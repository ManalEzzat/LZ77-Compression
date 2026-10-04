def find_longest_match(data, current_position,
                       window_size, lookahead_size): 
  search_window_start = max(0 , current_position - window_size) 
  lookAhead_end = min (len(data) , current_position + lookahead_size)
  search_buffer = data[search_window_start : current_position]
  lookahead_buffer = data[current_position : lookAhead_end]


  match_length = 0
  offset = 0
  for i in range(len(search_buffer)):
    length = 0
    while (length < len(lookahead_buffer) and
             (i + length) < len(search_buffer) and
           search_buffer[i + length] == lookahead_buffer[length] 
           ):
      length += 1

    if length > match_length:
      match_length = length
      offset = len(search_buffer) - i
      
  result = (offset , match_length)

  return result




