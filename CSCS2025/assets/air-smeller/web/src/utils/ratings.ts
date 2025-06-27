"use server";

interface Rating {
  comment: string;
  author: string;
  stars: number;
}

const UserRatings: Rating[] = [
  {
    comment:
      "The air feels incredibly fresh and revitalizing after purification. It's like breathing in a breath of fresh mountain air.",
    author: "Dr. Emily Carter",
    stars: 5,
  },
  {
    comment:
      "The purification process significantly improved the air quality. There's a noticeable reduction in odors, though a hint of chemical scent remains.",
    author: "Prof. James Liu",
    stars: 4,
  },
  {
    comment:
      "While the air is cleaner, I expected a more natural smell. It's better than before, but not quite what I hoped for.",
    author: "Mark Robinson",
    stars: 3,
  },
  {
    comment:
      "Absolutely transformed! The air is crisp and pure, reminiscent of a serene forest. I can breathe deeply without any discomfort.",
    author: "Sarah Thompson",
    stars: 5,
  },
  {
    comment:
      "The air purification has made a significant difference. It smells fresh and clean, although there's a slight residual scent from the purification process itself.",
    author: "Dr. Lisa Nguyen",
    stars: 4,
  },
];

export async function getRatings(): Promise<Rating[]> {
  return UserRatings;
}

export async function addRating(rating: Rating) {
  UserRatings.push(rating);
}
