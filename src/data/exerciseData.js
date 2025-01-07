export const exercises = [
  {
    slug: "bodyweight-squats",
    name: "Bodyweight Squats",
    description: "A bodyweight exercise to build lower body strength and core stability.",
    tags: ["Live Analysis", "Legs", "Bodyweight", "Strength", "Beginner"],
    muscleGroups: ["Quadriceps", "GluteusMaximus", "Hamstrings", "Abdominals"],
    instructions: [
      "Stand with feet shoulder-width apart, arms stretched forward at shoulder height.",
      "Engage your core and initiate the squat by pushing your hips back.",
      "Lower until thighs are parallel to the ground, keeping knees tracking over toes.",
      "Push through your heels to return to the starting position while maintaining arm alignment.",
    ],
    preferredCameraAngle: "Side View (90°)",
    angleReason: "This angle captures hip depth, knee tracking, and torso alignment without occlusion from the arms.",
    commonMistakes: [
      "Knees caving inward during the descent.",
      "Not lowering hips to at least parallel to the ground."
    ],
  },
  {
    slug: "deadlifts",
    name: "Deadlifts",
    description: "A compound movement that strengthens the posterior chain.",
    tags: ["Live Analysis", "Legs", "Barbell", "Strength", "Intermediate"],
    muscleGroups: ["Quadriceps", "GluteusMaximus", "Hamstrings", "LatissimusDorsi", "Trapezius"],
    instructions: [
      "Stand with the barbell over your midfoot and grip it just outside your knees.",
      "Hinge at your hips, keeping your back straight and lats engaged.",
      "Lift by extending your hips and knees simultaneously, keeping the bar close to your body.",
      "Lower the bar by reversing the movement, hinging at the hips first.",
    ],
    preferredCameraAngle: "Side View (90°)",
    angleReason: "This angle allows clear tracking of back alignment, hip hinge mechanics, and bar path.",
    commonMistakes: [
      "Rounding the lower back during the lift.",
      "Letting the bar drift away from the body."
    ],
  },
  {
    slug: "push-ups",
    name: "Push-Ups",
    description: "A classic bodyweight exercise for chest, shoulders, and triceps.",
    tags: ["Live Analysis", "Chest", "Bodyweight", "Strength", "Beginner"],
    muscleGroups: ["PectoralisMajor", "Deltoid", "Triceps", "Abdominals"],
    instructions: [
      "Start in a high plank with hands slightly wider than shoulder-width apart.",
      "Engage your core and lower your chest by bending your elbows to a 90-degree angle.",
      "Push through your palms to return to the starting position, maintaining a straight body line.",
    ],
    preferredCameraAngle: "Top Diagonal (30–45° Above)",
    angleReason: "This angle captures body alignment, elbow positioning, and depth of the movement.",
    commonMistakes: [
      "Allowing hips to sag or elevate during the movement.",
      "Flaring elbows excessively, placing strain on the shoulders."
    ],
  },
  {
    slug: "pull-ups",
    name: "Pull-Ups",
    description: "An upper body exercise focusing on back and biceps strength.",
    tags: ["Live Analysis", "Back", "Biceps", "Bodyweight", "Strength", "Advanced"],
    muscleGroups: ["LatissimusDorsi", "Biceps", "Trapezius", "Infraspinatus", "TeresMajor"],
    instructions: [
      "Grip the bar shoulder-width apart, palms facing away.",
      "Pull your chin above the bar by engaging your lats and squeezing your back.",
      "Lower yourself back to the starting position in a controlled manner.",
    ],
    preferredCameraAngle: "Front View (Head-On)",
    angleReason: "This angle allows clear visibility of grip width, elbow alignment, and range of motion.",
    commonMistakes: [
      "Using momentum or swinging the body to complete the movement.",
      "Not achieving full range of motion (chin above the bar)."
    ],
  },
  {
    slug: "bicep-curls",
    name: "Bicep Curls",
    description: "An isolation exercise for building bicep strength.",
    tags: ["Live Analysis", "Biceps", "Free Weight", "Isolation", "Beginner"],
    muscleGroups: ["Biceps", "Brachioradialis"],
    instructions: [
      "Stand with a dumbbell in each hand, palms facing forward.",
      "Curl the weights toward your shoulders, keeping elbows stationary.",
      "Lower the weights back to the starting position in a controlled motion.",
    ],
    preferredCameraAngle: "Front 45° View",
    angleReason: "This angle captures elbow stability, symmetry in arm movements, and proper curling motion.",
    commonMistakes: [
      "Swinging the torso to lift the weights.",
      "Elbows drifting forward or backward during the curl."
    ],
  },
  {
    slug: "weighted-forward-lunges",
    name: "Weighted Forward Lunges",
    description: "A dynamic unilateral exercise for lower body strength and balance.",
    tags: ["Live Analysis", "Legs", "Kettlebell", "Balance", "Strength", "Intermediate"],
    muscleGroups: ["Quadriceps", "GluteusMaximus", "Hamstrings", "Abdominals"],
    instructions: [
      "Hold a kettlebell/dumbell in a goblet position at chest height.",
      "Step forward and lower until both knees form a 90-degree angle.",
      "Ensure the front knee stays aligned over your ankle and torso remains upright.",
      "Push through your front heel to return to the starting position.",
    ],
    preferredCameraAngle: "Side View (90°)",
    angleReason: "This angle allows accurate tracking of knee alignment, hip movement, and torso stability during the lunge.",
    commonMistakes: [
      "Front knee extending beyond the toes.",
      "Leaning forward excessively instead of keeping the torso upright."
    ],
  },
  {
    slug: "russian-twist-situp-press",
    name: "Russian Twist Shoulder Press Sit-up",
    description: "A complex exercise combining core, shoulder, and rotational strength.",
    tags: ["Live Analysis", "Core", "Shoulders", "Dumbbell", "Strength", "Advanced"],
    muscleGroups: ["Abdominals", "ExternalOblique", "Deltoid"],
    instructions: [
      "Start seated, holding a dumbbell close to your chest.",
      "Perform a Russian twist by rotating your torso to each side.",
      "Lie back, then perform a sit-up while pressing the dumbbell overhead.",
      "Lower the dumbbell back to your chest and repeat the sequence.",
    ],
    preferredCameraAngle: "Front 45° View",
    angleReason: "This angle captures torso rotation, symmetry during the shoulder press, and sit-up depth.",
    commonMistakes: [
      "Rotating arms without proper torso engagement during the twist.",
      "Failing to maintain control of the dumbbell during the press."
    ],
  },
];
