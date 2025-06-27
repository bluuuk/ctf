"use client";

import { addRating } from "@/utils/ratings";
import { useState } from "react";
import { StarsInput } from "./stars_input";

function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export const RatingInput = () => {
  const [content, setContent] = useState<string>("");
  const [author, setAuthor] = useState<string>("");
  const [stars, setStars] = useState<number>(0);

  const submitPressed = () => {
    addRating({
      comment: content,
      author: author,
      stars: stars,
    });

    sleep(1000);
    window.location.reload();
  };

  return (
    <div className="">
      <div className="font-bold">Leave your own rating:</div>
      <div className="rounded-lg border p-2 bg-indigo-200">
        <StarsInput setStarValue={setStars} />
        <div>Comment:</div>
        <textarea
          className="p-1 block w-full rounded mb-4"
          onChange={(e) => setContent(e.target.value)}
        />
        <div>Author:</div>
        <input
          className="p-1 block w-full rounded"
          type="text"
          onChange={(e) => setAuthor(e.target.value)}
        />
        <input
          className="cursor-pointer mt-8 w-full block bg-indigo-500 rounded-md px-2.5 py-1.5 text-white hover:bg-indigo-800 focus:ring-4 focus:ring-indigo-200"
          type="button"
          value="Submit"
          onClick={submitPressed}
        />
      </div>
    </div>
  );
};
