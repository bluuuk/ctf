export const dynamic = 'force-dynamic'

import { RatingInput } from "@/components/rating_input";
import { Ratings } from "@/components/ratings";

export default function Home() {
  return (
    <div className="flex justify-center	align-center m-10">
      <div className="max-w-2xl w-full">
        <div className="">
          <Ratings />
        </div>
        <RatingInput />
      </div>
    </div>
  );
}
