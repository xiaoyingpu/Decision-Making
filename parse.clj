(defn pipe [s]
  (str 
   (apply str 
          (interpose "|" s))
   \newline
   (apply str 
          (interpose "|" 
                     (for [token s]
                       "--")))))
