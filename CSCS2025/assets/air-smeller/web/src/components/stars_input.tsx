import { IconStar, IconStarFilled } from "@tabler/icons-react";
import { useEffect, useState } from "react";

const Star = ({ active }: { active: boolean }) => {
  return (
    <>
      {active ? (
        <IconStarFilled className="cursor-pointer text-yellow-500" stroke={2} />
      ) : (
        <IconStar className="cursor-pointer text-yellow-500" stroke={2} />
      )}
    </>
  );
};

export const StarsInput = ({
  setStarValue,
}: {
  setStarValue: (vlaue: number) => void;
}) => {
  const [value, setValue] = useState<number>(1);

  useEffect(() => {
    setStarValue(value);
  }, [setStarValue, value]);

  return (
    <div className="block">
      <input
        className="hidden"
        type="radio"
        name="star-rating"
        id="star-rating-1"
        onChange={() => setValue(1)}
      />
      <label className="inline-flex" htmlFor="star-rating-1">
        <Star active={value >= 1} />
      </label>
      <input
        className="hidden"
        type="radio"
        name="star-rating"
        id="star-rating-2"
        onChange={() => setValue(2)}
      />
      <label className="inline-flex" htmlFor="star-rating-2">
        <Star active={value >= 2} />
      </label>
      <input
        className="hidden"
        type="radio"
        name="star-rating"
        id="star-rating-3"
        onChange={() => setValue(3)}
      />
      <label className="inline-flex" htmlFor="star-rating-3">
        <Star active={value >= 3} />
      </label>
      <input
        className="hidden"
        type="radio"
        name="star-rating"
        id="star-rating-4"
        onChange={() => setValue(4)}
      />
      <label className="inline-flex" htmlFor="star-rating-4">
        <Star active={value >= 4} />
      </label>
      <input
        className="hidden"
        type="radio"
        name="star-rating"
        id="star-rating-5"
        onChange={() => setValue(5)}
      />
      <label className="inline-flex" htmlFor="star-rating-5">
        <Star active={value >= 5} />
      </label>
    </div>
  );
};
