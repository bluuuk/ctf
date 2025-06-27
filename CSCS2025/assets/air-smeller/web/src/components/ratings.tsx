"use server";

import { getRatings } from "@/utils/ratings";
import { JSDOM } from "jsdom";
import DOMPurify from "dompurify";
import { Stars } from "./stars";

export const Ratings = async () => {
  const window = new JSDOM("").window;
  const purify = DOMPurify(window);

  return (
    <div>
      <div className="font-bold">
        What other people said about the smell of our purifier:
      </div>
      {(await getRatings()).map((r, i) => (
        <div key={i} className="flex bg-white p-2 flex-col">
          <div className="rounded-lg border p-2 w-full bg-blue-200">
            <Stars value={r.stars} />
            <div
              dangerouslySetInnerHTML={{ __html: purify.sanitize(r.comment) }}
            />
          </div>
          <div className="w-full flex">
            <div className="text-sm ml-auto self-start">{r.author}</div>
          </div>
        </div>
      ))}
    </div>
  );
};
