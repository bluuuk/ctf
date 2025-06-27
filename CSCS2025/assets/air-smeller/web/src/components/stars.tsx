import { IconStar, IconStarFilled } from "@tabler/icons-react";

const Star = ({ active }: { active: boolean }) => {
  return (
    <>
      {active ? (
        <IconStarFilled className="text-yellow-500" stroke={2} />
      ) : (
        <IconStar className="text-yellow-500" stroke={2} />
      )}
    </>
  );
};

export const Stars = ({ value }: { value: number }) => {
  return (
    <div className="block">
      <div className="inline-flex">
        <Star active={value >= 1} />
      </div>
      <div className="inline-flex">
        <Star active={value >= 2} />
      </div>
      <div className="inline-flex">
        <Star active={value >= 3} />
      </div>
      <div className="inline-flex">
        <Star active={value >= 4} />
      </div>
      <div className="inline-flex">
        <Star active={value >= 5} />
      </div>
    </div>
  );
};
