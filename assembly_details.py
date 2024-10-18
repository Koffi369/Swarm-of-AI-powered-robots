

# Every detail position and target position is defined in global frame
# every detail component is defined in detail local frame
# global frame is aruco marker frame


# Target position is a position of local detail frame in global frame
# Mounting hole is position on mounting hole in local detail frame


{
  "assembly": {
      
    "base": {
      "position": { "x": 0, "y": 0, "alpha": 0},
      "pins": [
        {
          "id": 1,
          "position": { "x": -25, "y": 0, "alpha": 0}
        },
        {
          "id": 2,
          "position": { "x": 25, "y": 0, "alpha": 0}
        }
      ]
    },

      
    "parts": [
        
      {
        "id": "part_1",
        "position": { "x": -8, "y": -60, "alpha": 0},
        "target_position": {"x": -25,  "y": 0,  "alpha": 0},
          
        "mounting_hole": {
          "id": 1,
          "position": { "x": 0,"y": 0,"alpha": 0}
        },
        "grip_pin": {
          "position": {"x": -40,"y": 15,"alpha": 0}
        }
      },
        
      {
        "id": "part_2",
        "position": {"x": 8,"y": -60, "alpha": 0},
        "target_position": {"x": 25,"y": 0, "alpha": 0},
          
        "mounting_hole": {
          "id": 2,
          "position": {"x": 0,"y": 0,"alpha": 0}
        },
        "grip_pin": {"position": {"x": 40,"y": 15, "alpha": 0
          }
        }
      }
    ]
  }
}


