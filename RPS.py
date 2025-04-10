def player(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
        
    opponent_history.append(prev_play)
    
    # Default move
    guess = "R"
    
    if len(opponent_history) > 10:
        # Look for patterns in the last few moves
        
        # Pattern based on the last move (counter the move that would beat their last move)
        last_move = opponent_history[-1]
        if last_move == "R":
            counter_last = "P"  # Paper beats Rock
        elif last_move == "P":
            counter_last = "S"  # Scissors beats Paper
        else:
            counter_last = "R"  # Rock beats Scissors
            
        # Count frequencies of opponent's moves
        r_count = opponent_history.count("R")
        p_count = opponent_history.count("P")
        s_count = opponent_history.count("S")
        
        # Get the most frequent move
        most_frequent = "R"
        if p_count > r_count and p_count > s_count:
            most_frequent = "P"
        elif s_count > r_count and s_count > p_count:
            most_frequent = "S"
            
        # Counter for most frequent move
        if most_frequent == "R":
            counter_frequent = "P"
        elif most_frequent == "P":
            counter_frequent = "S"
        else:
            counter_frequent = "R"
            
        # Look for patterns in the last 4 moves
        if len(opponent_history) > 4:
            last_four = "".join(opponent_history[-4:])
            potential_pattern = "".join(opponent_history[-3:])
            
            # Check the history for this pattern
            pattern_matches = []
            for i in range(len(opponent_history) - 3):
                if "".join(opponent_history[i:i+3]) == potential_pattern:
                    pattern_matches.append(opponent_history[i+3])
            
            # If we found this pattern before, counter what usually comes next
            if pattern_matches:
                # Count what comes after this pattern most often
                r_after = pattern_matches.count("R")
                p_after = pattern_matches.count("P")
                s_after = pattern_matches.count("S")
                
                prediction = "R"
                if p_after > r_after and p_after > s_after:
                    prediction = "P"
                elif s_after > r_after and s_after > p_after:
                    prediction = "S"
                
                # Return the counter to the prediction
                if prediction == "R":
                    return "P"
                elif prediction == "P":
                    return "S"
                else:
                    return "R"
        
        # If no strong pattern detected, use a mix of counters to recent moves
        # Use counter to most frequent move 60% of the time
        # Use counter to last move 40% of the time
        import random
        if random.random() < 0.6:
            guess = counter_frequent
        else:
            guess = counter_last
    
    # For the first few moves or if no pattern detected
    return guess